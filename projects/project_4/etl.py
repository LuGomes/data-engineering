import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, monotonically_increasing_id, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek, date_format
from pyspark.sql.types import TimestampType, DateType


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']

def create_spark_session():
    """Create a Spark Session which is our entrypoint to programming with Spark while making use of dataframes."""

    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .config("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.awsAccessKeyId", os.environ['AWS_ACCESS_KEY_ID']) \
        .config("spark.hadoop.fs.s3a.awsSecretAccessKey", os.environ['AWS_SECRET_ACCESS_KEY']) \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Perform ETL from songs metadata to songs and artists dimensions. 
    The input JSON files are read into a dataframe, from which the songs and artists dataframes are created by selection of relevant columns. Duplicates are dropped in both cases.
    The resulting dataframes are uploaded back into S3 as parquet files. 
    The songs parquet files are partitioned by year and artist whereas a single artists parquet file is stored in S3.
    
    Keyword arguments:
    spark -- the spark session instance
    input_data -- the path of the AWS S3 bucket that contains the input data
    output_data -- the path of the AWS S3 bucket that will store the ETL output data
    """
    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data/*/*/*/*.json")

    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year", "artist_id").parquet(output_data + "songs")

    # extract columns to create artists table
    artists_table = df.select("artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude").dropDuplicates()
    
    # write artists table to parquet files
    artists_table.write.parquet(output_data + "artists")


def process_log_data(spark, input_data, output_data):
    """
    Perform ETL from songplays to users and time dimensions as well as songplays fact. 
    The input JSON files are read into a dataframe and filtered for NextSong page type.
    The resulting dataframes are uploaded back into S3 as parquet files. 
    The time and songplays parquet files are partitioned by year and month whereas a single users parquet file is stored in S3.
    
    Keyword arguments:
    spark -- the spark session instance
    input_data -- the path of the AWS S3 bucket that contains the input data
    output_data -- the path of the AWS S3 bucket that will store the ETL output data
    """
        
    # get filepath to log data file
    log_data = os.path.join(input_data, "log-data/*/*/*.json")

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter(df["page"] == 'NextSong')

    # extract columns for users table    
    users_table = df.select("userid", "firstname", "lastname", "gender", "level").dropDuplicates()

    # write users table to parquet files
    users_table.write.parquet(output_data + "users")

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda ts: datetime.fromtimestamp(int(ts)/1000.0), TimestampType())
    df = df.withColumn("timestamp", get_timestamp(df.ts))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda ts: datetime.fromtimestamp(int(ts)/1000.0), DateType())
    df = df.withColumn("start_time", get_datetime(df.ts))
    
    # extract columns to create time table
    time_table = df.selectExpr('start_time') \
        .dropDuplicates() \
        .orderBy('start_time', ascending=True) \
        .withColumn('hour', hour('start_time')) \
        .withColumn('day', dayofmonth('start_time')) \
        .withColumn('week', weekofyear('start_time')) \
        .withColumn('month', month('start_time')) \
        .withColumn('year', year('start_time')) \
        .withColumn('weekday', dayofweek('start_time'))    
    
    # write time table to parquet files partitioned by year and month
    time_table = time_table.write.partitionBy("year", "month").parquet(output_data + "time")

    # read in song data to use for songplays table
    song_df = spark.read.json(os.path.join(input_data, "song_data/*/*/*/*.json"))

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df.join(song_df, df['song'] == song_df['title']).select(monotonically_increasing_id().alias('songplay_id'), \
                                                                              'start_time', \
                                                                              col('userId').alias('user_id'), \
                                                                              'level', \
                                                                              'song_id', \
                                                                              'artist_id', \
                                                                              col('sessionId').alias('session_id'), \
                                                                              'location', \
                                                                              col('userAgent').alias('user_agent'))
    
    songplays_table.join(time_table, songplays_table.start_time == time_table.start_time, how='inner').select('songplay_id', songplays_table.start_time, 'user_id', 'level', 'song_id', \
    'artist_id', 'session_id', 'location', 'user_agent', time_table.year, time_table.month)
    
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year", "month").parquet(output_data + "songplays")


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://sparkify-lugomes/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
