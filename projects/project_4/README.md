### The Project

A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a **data lake**. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, we build an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.


### Project Structure
This project contains the following files:

- `etl.py`: python script that performs ETL - loads data from S3 and transform them into dimensional tables that are saved to parquet files back in S3, partitioned as needed.
- `dl.cfg`: configuration file with variables needed to access AWS services.

### How to run

- Launch an EMR cluster with Spark pre-installed and attach your a previously generated key to it.
- Connect to the EMR cluster from the terminal using SSH: `ssh -i <keyfile_path> <hadoop@ec2-***.compute.amazonaws.com>`.
- Copy the files from your local environment into the cluster: `scp -i <keyfile_path> etl.py dl.cfg hadoop@ec2-***.compute.amazonaws.com:~/` (where `<keyfile_path>=~/Downloads/spark.pem` if you have the key file on your local downloads folder and `hadoop@ec2-***.compute.amazonaws.com` can be found in the AWS dashboard under master public DNS)
- Submit the application to the EMR cluster: `spark-submit --master yarn ./etl.py` which will trigger the run.
- After successful execution, you should be able to see the transformed data in the dimensional tables in S3, partitioned where applicable.

### Details/insights

This database can be used by the business to track multiple metrics that are ultimately insights into helping the business grow.

Below are just a few examples:

- what location is the app lacking traction
- what user agent requires better experience
- what songs/artists are popular and could be promoted, more songs could be added to database from trending artists
- which users are listening less, stopped listening - reach out to those people
- what is the proportion of free/paid tiers and difference in listening time between them - maybe some subscription discount to gain traction is worthwhile
- what time of day, year do people listen less to music - increase marketing efforts during those periods, maybe promotion


### Database Schema design and ETL pipeline

The schema used is the STAR with one fact table (that drives business analytics) and four dimension tables (that provide more info on pieces). This schema is justified since it provides flexibility in executing ad hoc queries with fast aggregations.

### ETL

From two types of JSON files, we create one facts table (`songplays`) and four dimensions tables (`users`, `artists`, `songs` and `time`) by selecting relevant data columns and performing simple transformations. The resulting dataframes are loaded back into S3 in the parquet format. To more easily see the results, we partition the data into the S3 folders as follows:

- Songs table files are partitioned by year and then artist.
- Time table files are partitioned by year and month.
- Songplays table files are partitioned by year and month.
