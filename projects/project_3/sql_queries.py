import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
DWH_ROLE_ARN = config.get('IAM_ROLE','ARN')
S3_LOG_DATA = config.get('S3','LOG_DATA')
S3_SONG_DATA = config.get('S3','SONG_DATA')
LOG_JSONPATH = config.get('S3', 'LOG_JSONPATH')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE staging_events (
                                 artist             TEXT,
                                 auth               VARCHAR(10) NOT NULL,
                                 firstName          TEXT,
                                 gender             VARCHAR(1),
                                 itemInSession      INT2 NOT NULL,
                                 lastName           TEXT,
                                 length             NUMERIC(9,5),
                                 level              VARCHAR(4) NOT NULL,
                                 location           TEXT,
                                 method             VARCHAR(3) NOT NULL,
                                 page               VARCHAR(20) NOT NULL,
                                 registration       NUMERIC(16,1),
                                 sessionId          INT4 NOT NULL,
                                 song               TEXT,
                                 status             INT4 NOT NULL,
                                 ts                 INT8 NOT NULL,
                                 userAgent          TEXT,
                                 userId             INT4
);
""");

staging_songs_table_create = ("""CREATE TABLE staging_songs (
                                 num_songs          INT2 NOT NULL,
                                 artist_id          VARCHAR(18) NOT NULL,
                                 artist_lattitude   NUMERIC(8,5),
                                 artist_longitude   NUMERIC(8,5),
                                 artist_location    TEXT NOT NULL,
                                 artist_name        TEXT NOT NULL,
                                 song_id            VARCHAR(18) NOT NULL,
                                 title              TEXT NOT NULL,
                                 duration           NUMERIC(9,5) NOT NULL,
                                 year               INT4 NOT NULL
);
""");

songplay_table_create = ("""CREATE TABLE songplays (
                            songplay_id            INT4 IDENTITY(0,1),
                            start_time             INT8 NOT NULL,
                            user_id                VARCHAR(4),    
                            level                  VARCHAR(4) NOT NULL,
                            song_id                VARCHAR(18) NOT NULL,
                            artist_id              VARCHAR(18) NOT NULL,
                            session_id             INT4 NOT NULL,
                            location               TEXT,
                            user_agent             TEXT
);
""");

user_table_create = ("""CREATE TABLE users (
                        user_id                    INT4 PRIMARY KEY, 
                        first_name                 TEXT, 
                        last_name                  TEXT, 
                        gender                     VARCHAR(1) NOT NULL, 
                        level                      VARCHAR(4) NOT NULL
);
""");

song_table_create = ("""CREATE TABLE songs (
                        song_id                    VARCHAR(18) PRIMARY KEY, 
                        title                      TEXT NOT NULL, 
                        artist_id                  VARCHAR(18) NOT NULL, 
                        year                       INT4 NOT NULL, 
                        duration                   NUMERIC(9,5) NOT NULL
);
""");

artist_table_create = ("""CREATE TABLE artists (
                          artist_id                VARCHAR(18) PRIMARY KEY, 
                          name                     TEXT NOT NULL,  
                          location                 TEXT NOT NULL, 
                          lattitude                NUMERIC(8,5), 
                          longitude                NUMERIC(8,5)
);
""");

time_table_create = ("""CREATE TABLE time (
                        start_time                 TIMESTAMP NOT NULL, 
                        hour                       INT2 NOT NULL, 
                        day                        INT2 NOT NULL, 
                        week                       INT2 NOT NULL, 
                        month                      INT2 NOT NULL, 
                        year                       INT4 NOT NULL, 
                        weekday                    INT2 NOT NULL
);
""");

# STAGING TABLES

staging_events_copy = ("""COPY staging_events
                          FROM {}
                          IAM_ROLE {}
                          JSON {}
                          REGION 'us-west-2'
""").format(S3_LOG_DATA, DWH_ROLE_ARN, LOG_JSONPATH);

staging_songs_copy = ("""COPY staging_songs
                          FROM {}
                          IAM_ROLE {}
                          JSON 'auto'
                          REGION 'us-west-2'
""").format(S3_SONG_DATA, DWH_ROLE_ARN);

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplays
                            (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            SELECT DISTINCT
                            e.ts,e.userId,e.level,s.song_id,s.artist_id,e.sessionId,s.artist_location,e.userAgent
                            FROM staging_events e
                            JOIN staging_songs s
                            ON (e.artist = s.artist_name) AND (e.song = s.title)
""");

user_table_insert = ("""INSERT INTO users
                        (user_id, first_name, last_name, gender, level)
                        SELECT DISTINCT userId,firstName,lastName,gender,level
                        FROM staging_events
                        WHERE page='NextSong'
""");

song_table_insert = ("""INSERT INTO songs
                        (song_id, title, artist_id, year, duration)
                        SELECT DISTINCT song_id, title,artist_id,year,duration
                        FROM staging_songs
""");

artist_table_insert = ("""INSERT INTO artists
                          (artist_id, name, location, lattitude, longitude)
                          SELECT DISTINCT artist_id, artist_name, artist_location, artist_lattitude, artist_longitude
                          FROM staging_songs
""");

time_table_insert = ("""INSERT INTO time 
                        (start_time, hour, day, week, month, year, weekday)
                        SELECT a.start_time,
                        EXTRACT (HOUR FROM a.start_time), EXTRACT (DAY FROM a.start_time),
                        EXTRACT (WEEK FROM a.start_time), EXTRACT (MONTH FROM a.start_time),
                        EXTRACT (YEAR FROM a.start_time), EXTRACT (WEEKDAY FROM a.start_time) FROM
                        (SELECT TIMESTAMP 'epoch' + start_time/1000 *INTERVAL '1 second' as start_time FROM songplays) a;
""");

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
