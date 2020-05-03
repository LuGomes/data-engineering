## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
This database can be used by the business to track multiple metrics that are ultimately insights into helping the business grow. 
Below are just a few examples:
- what location is the app lacking traction
- what user agent requires better experience
- what songs/artists are popular and could be promoted/trend, more songs added to database from trending artists
- which users are listening less, stopped listening - reach out to those people
- what is the proportion of free/paid tiers and difference in listening time between them
- what time of day, year do people listen less to music - increase marketing efforts during those periods, maybe promo?

## State and justify your database schema design and ETL pipeline.
The schema used is the star with one fact table (that drives business analytics) and four dimension tables (that provide more info on pieces). This schema is justified since it provides flexibility in executing ad hoc queries with fast aggregations.
Our ETL process was fairly simple, with not much transformation of data. Our json files were loaded into dataframes so we could select colums of interest and partition the data into the data model of choice. The types of variables need to be carefully defined based on what types came in through the json files.

## Provide example queries and results for song play analysis.
Some examples:
- proportion of active users in different countries or different regions of the same country - where to promote the app
- proportion of users in free vs paid tiers - maybe membership is too expensive, do promo to gain traction ?
- proportion of users that use each agent to listen to songs - where should we improve the UX more?
- ...

