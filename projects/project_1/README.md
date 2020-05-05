## The Project

In this project, we model user activity data for a music streaming app called `Sparkify`. We create a Postgres database instance, import data stored in JSON files, and model the data using a relational model in Postgres. We define Fact and Dimension tables and insert data into them. The Fact table ultimately can be used to build understanding on what songs users of the app are listening to, helping the business grow.

## Project Structure

This project contains the following files/folders:
- `data`: folder with JSON files with the data for the project
- `create_tables.py`: python script that creates the Postgres tables
- `etl.py`: python script that performs ETL - extract data from the JSON files, transforms and load into the Postgres tables.
- `etl.ipynb`: Jupyter notebook to test the ETL process without loading the entire dataset.
- `sql_queries.py`: python script that defines our SQL queries to create tables, insert data into them as well as dropping tables after work is complete.

## How to run

- In the command prompt, run the `create_tables.py` script to create the Postgres tables.
- In the command prompt, run the `etl.py` script to extract data from json files (files in `data` folder) and insert relevant data into the Postgres tables.
- To see the resulting tables, run the Jupyter notebook `test.ipynb`.

## Details/insights  

### The purpose of this database in the context of the startup, Sparkify, and their analytical goals

This database can be used by the business to track multiple metrics that are ultimately insights into helping the business grow. 

Below are just a few examples:
- what location is the app lacking traction
- what user agent requires better experience
- what songs/artists are popular and could be promoted/trend, more songs added to database from trending artists
- which users are listening less, stopped listening - reach out to those people
- what is the proportion of free/paid tiers and difference in listening time between them
- what time of day, year do people listen less to music - increase marketing efforts during those periods, maybe promo?

### Database Schema design and ETL pipeline
The schema used is the **STAR** with one fact table (that drives business analytics) and four dimension tables (that provide more info on pieces). This schema is justified since it provides flexibility in executing ad hoc queries with fast aggregations.

![ETL](./ETL.png)

Our ETL process is fairly simple, with not much transformation of data. Our JSON files are loaded into dataframes so we can select colums of interest and partition the data into the data model of choice. The types of variables need to be carefully defined based on what types came in through the JSON files.

### Example queries and results for song play analysis
Some examples:
- proportion of active users in different countries or different regions of the same country - where to promote the app
- proportion of users in free vs paid tiers - maybe membership is too expensive, do promo to gain traction ?
- proportion of users that use each agent to listen to songs - where should we improve the UX more?
- ...

