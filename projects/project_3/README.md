### The Project
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, we build an ETL pipeline for a database hosted on Redshift. The pipeline extracts Sparkify’s data from S3, stages the data in Amazon Redshift and transforms data into a set of fact and dimensional tables which can then be used by the Sparkify analytics team to continue finding insights in what songs their users are listening to.

### Project Structure
This project contains the following files/folders:

`create_tables.py`: python script that creates the tables on Redshift.
`etl.py`: python script that performs ETL - copies data from S3 into staging tables and then data from these tables into the fact and dimensional tables on Redshift.
`sql_queries.py`: python script that defines our SQL queries to create tables, insert data into them as well as dropping tables after work is complete.
`dwh.cfg`: configuration file with variables needed to access the Redshift cluster and create/load data into its tables.

### How to run
In the command prompt, run the create_tables.py script to create the staging and fact/dimensional tables on Redshift.
In the command prompt, run the etl.py script to copy data from S3 into the staging tables as well as extract, transform and load data from the staging tables into the Star schema tables.
After that, the Redshift query editor can be used to query the database for business insights.

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

Our ETL process is fairly simple, with not much transformation of data. From our staging tables we can select colums of interest and partition the data into the data model of choice. The types of variables need to be carefully defined based on what types came in through the JSON files.
