## Data Engineering Nanodegree - [Udacity](https://www.udacity.com/course/data-engineer-nanodegree--nd027)

### Section 1 - Introduction to Data Engineering

Why? Vital role in storing, organizing and making use of data.

**The Project Journey**
The projects will take you on a journey where you’ll assume the role of a Data Engineer at a fabricated data streaming company called “Sparkify” as it scales its data engineering in both size and sophistication. You’ll work with simulated data of listening behavior, as well as a wealth of metadata related to songs and artists. You’ll start working with a small amount of data, with low complexity, processed and stored on a single machine. By the end, you’ll develop a sophisticated set of data pipelines to work with massive amounts of data processed and stored on the cloud. There are five projects in the program. Below is a description of each.

**Project 1 - Data Modeling**
In this project, you’ll model user activity data for a music streaming app called Sparkify. The project is done in two parts. You’ll create a database and import data stored in CSV and JSON files, and model the data. You’ll do this first with a relational model in Postgres, then with a NoSQL data model with Apache Cassandra. You’ll design the data models to optimize queries for understanding what songs users are listening to. For PostgreSQL, you will also define Fact and Dimension tables and insert data into your new tables. For Apache Cassandra, you will model your data to help the data team at Sparkify answer queries about app usage. You will set up your Apache Cassandra database tables in ways to optimize writes of transactional data on user sessions.

**Project 2 - Cloud Data Warehousing**
In this project, you’ll move to the cloud as you work with larger amounts of data. You are tasked with building an ELT pipeline that extracts Sparkify’s data from S3, Amazon’s popular storage system. From there, you’ll stage the data in Amazon Redshift and transform it into a set of fact and dimensional tables for the Sparkify analytics team to continue finding insights in what songs their users are listening to.

**Project 3 - Data Lakes with Apache Spark**
In this project, you'll build an ETL pipeline for a data lake. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the app. You will load data from S3, process the data into analytics tables using Spark, and load them back into S3. You'll deploy this Spark process on a cluster using AWS.

**Project 4 - Data Pipelines with Apache Airflow**
In this project, you’ll continue your work on Sparkify’s data infrastructure by creating and automating a set of data pipelines. You’ll use the up-and-coming tool Apache Airflow, developed and open-sourced by Airbnb and the Apache Foundation. You’ll configure and schedule data pipelines with Airflow, setting dependencies, triggers, and quality checks as you would in a production setting.

**Project 5 - Data Engineering Capstone**
The capstone project is an opportunity for you to combine what you've learned throughout the program into a more self-driven project. In this project, you'll define the scope of the project and the data you'll be working with. We'll provide guidelines, suggestions, tips, and resources to help you be successful, but your project will be unique to you. You'll gather data from several different data sources; transform, combine, and summarize it; and create a clean database for others to analyze.

**What is Data Engineering**

Data Engineering comprises all engineering and operational tasks required to make data available for the end-user, whether for the purposes of analytics, model building, app development, etc.

![](./images/1.png)
![](./images/2.png)
![](./images/3.png)
![](./images/4.png)

For the most part, Data Engineering design efficient ways to store data, running pipelines to transform and move data and prepping data by cleaning and summarizing to help the end-user. Core role is storing data in data warehouses and data lakes and running data pipelines!

1) [On the Evolution of Data Engineering](https://medium.com/analytics-and-data/on-the-evolution-of-data-engineering-c5e56d273e37): This short read (~5 minutes) focuses on the recent change from managing SQL databases to working with massive datasets in real time. It was written by Julien Kervizic, an experienced analytics expert from the Netherlands.

2) [Data Engineering Introduction and Epochs](https://learn.panoply.io/hubfs/Data%20Engineering%20-%20Introduction%20and%20Epochs.pdf): This slightly longer read (~20 minutes) goes further back in time to the birth of computers. It walks through four "epochs" of data engineering, and the major advances over the past 70 years. It was written by Panopoly, a data engineering platform provider.

**Data Engineering Tools**

- https://www.burtchworks.com/2018/09/10/the-rise-of-data-engineering-common-skills-and-tools/
- https://www.analyticsindiamag.com/data-engineering-101-top-tools-and-framework-resources/
- https://joviam.com/this-infographic-of-big-data-tools-will-blow-your-mind-infographic/
- https://datafloq.com/big-data-open-source-tools/os-home/

### Section 2 - Data Modeling

#### Lesson 1 - Introduction to Data Modeling

> In this lesson, students will learn the basic difference between relational and non-relation databases, and how each type of database fits the diverse needs of data consumers. 

**What is a Data Model?**

> "... an abstraction that organizes elements of data and how they relate to each other" --Wikipedia
> Data Modeling can easily translate to database modeling, as this is the essential end state.

**Common Questions**

1. Why can't everything be stored in a giant Excel spreadsheet?

There are limitations to the amount of data that can be stored in an Excel sheet. So, a database helps organize the elements into tables - rows and columns, etc. Also reading and writing operations on a large scale is not possible with an Excel sheet, so it's better to use a database to handle most business functions.

2. Does data modeling happen before you create a database, or is it an iterative process?

It's definitely an iterative process. Data engineers continually reorganize, restructure, and optimize data models to fit the needs of the organization.

3. How is data modeling different from machine learning modeling?

Machine learning includes a lot of data wrangling to create the inputs for machine learning models, but data modeling is more about how to structure data to be used by different people within an organization. You can think of data modeling as the process of designing data and making it available to machine learning engineers, data scientists, business analytics, etc., so they can make use of it easily.

![](./images/5.png)

We focus on the physical data model to create Data Definition Languages (DDL's) in Relational and Non-Relational databases.

- Data organization is critical!
- Organized data determines later data use. Queries that could have been straightforward and simple might become complicated queries if data modeling isn't well thought out.
- Begin prior to building out application, business logic and analytic models.
- Iterative process! Data modeling is not a fixed process. It is iterative as new requirements and data are introduced. Having flexibility will help as new information becomes available.

**Relational vs NoSQL Databases**

**Relational Model**

The software system used to maintain relational databases is a relational database management system or **RDBMS**. Invented by IBM in the late 60s.
Structured Query Language or **SQL** is the language used across almost all relational database systems for querying and maintaining the database.
Examples: Oracle, Teradata, MySql, PostgreSQL, Sqlite.

A **Schema** is a collection of tables. **Tables/Relation** is a group of rows sharing the same labeled elements. **Columns/Attributes** are labeled elements. **Rows/Tuple** is a single item.

![](./images/6.png)

**When to Use a Relational Database**

- Ease of use -- SQL
- Ability to do JOINS
- Ability to do aggregations and analytics
- Smaller data volumes - not Big Data!
- Easier to change to business requirements
- Flexibility for queries
- Modeling the data not modeling the queries
- Secondary Indexes available: You have the advantage of being able to add another index to help with quick searching.
- ACID Transactions: Allows you to meet a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, and thus maintain data integrity.

**ACID Transactions**

> "... properties of database transactions intended to guarantee validity even in the event of errors, power failures,..." -- Wikipedia

**Atomicity**: The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created.

**Consistency**: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables.

**Isolation**: Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other.

**Durability**: Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs.

**When Not to Use a Relational Database**

- Have large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.
- Need to be able to store different data type formats: Relational databases are not designed to handle unstructured data.
- Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.
- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
- Need high availability: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.

**High Availability** - describes a database where there is very little **downtime** of the system, it is always **on** and **functioning**.
**Horizontal Scalability** - ability to add more nodes/servers to the system to increase performance.

**What is PostgreSQL**

- Open source object-relational database system
- Uses and builds on SQL language
- Refer to `Lesson 1 Demo 0`, `Lesson 1 Demo 1`, `Lesson 1 Exercise 1`.

**NoSQL Databases**

> "... has a simpler design, simpler horizontal scaling, and finer control of availability. Data structures used are different than those in Relational Databases nd they make some operations faster.

- NoSQL and NonRelational are interchangeable.
- Also invented in the late 70s but became more popular in the 2000s as data sizes became bigger and less downtimes became acceptable. It was built to solve the limitations of the Relational DBs.
- Apache Cassandra (Partition Row Store) | MongoDB (Document Store) | DynamoDB (Key-Value Store) | Apache HBase (Wide Column Store) | Neo4J (Graph Database)
- Specific to Apache Cassandra: `Keyspace` (collection of tables), `Table` (Group of partitions) and `Rows` (single item).

![](./images/7.png)

**Apache Cassandra**

> "... provides scalability and high availability without compromising performance. Linear Scalability and proven fault-tolerance on commodity hardware or cloud infrastructure make it perfect platform for mission-critical data."

- Uses its own query language CQL.

What type of companies use Apache Cassandra?

All kinds of companies. For example, Uber uses Apache Cassandra for their entire backend. Netflix uses Apache Cassandra to serve all their videos to customers. Good use cases for NoSQL (and more specifically Apache Cassandra) are:

- Transaction logging (retail, health care)
- Internet of Things (IoT)
- Time series data
- Any workload that is heavy on writes to the database (since Apache Cassandra is optimized for writes).

Would Apache Cassandra be a hindrance for my analytics work? If yes, why?

Yes, if you are trying to do analysis, such as using `GROUP BY` statements. Since Apache Cassandra requires data modeling based on the query you want, you can't do ad-hoc queries. However you can add clustering columns into your data model and create new tables.

**When to use a NoSQL Database**

- Need to be able to store different data type formats: NoSQL was also created to handle different data configurations: structured, semi-structured, and unstructured data. JSON, XML documents can all be handled easily with NoSQL.
- Large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. NoSQL databases were created to be able to be horizontally scalable. The more servers/systems you add to the database the more data that can be hosted with high availability and low latency (fast reads and writes).
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data
- Need high throughput: While ACID transactions bring benefits they also slow down the process of reading and writing data. If you need very fast reads and writes using a relational database may not suit your needs.
- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
- Need high availability: Relational databases have a single point of failure. When that database goes down, a failover to a backup system must happen and takes time.

So bottom line: built for Big Data and to provide users with low latency.

**When NOT to use a NoSQL Database**

- When you have a small dataset: NoSQL databases were made for big datasets not small datasets and while it works it wasn’t created for that.
- When you need ACID Transactions: If you need a consistent database with ACID transactions, then most NoSQL databases will not be able to serve this need. NoSQL database are eventually consistent and do not provide ACID transactions. However, there are exceptions to it. Some non-relational databases like MongoDB can support ACID transactions.
- When you need the ability to do JOINS across tables: NoSQL does not allow the ability to do JOINS. This is not allowed as this will result in full table scans.
- If you want to be able to do aggregations and analytics.
- If you have changing business requirements: Ad-hoc queries are possible but difficult as the data model was done to fix particular queries.
- If your queries are not available and you need the flexibility: You need your queries in advance. If those are not available or you will need to be able to have flexibility on how you query your data you might need to stick with a relational database.

*Caveats to NoSQL and ACID Transactions*
There are some NoSQL databases that offer some form of ACID transaction. As of v4.0, MongoDB added multi-document ACID transactions within a single replica set. With their later version, v4.2, they have added multi-document ACID transactions in a shared/partitioned deployment.

> NoSQL databases and Relational databases do not replace each other for all tasks. Both do different tasks extremely well, and should be utilized for the use cases they fit best.

- Does not allow for duplicates as opposed to PostgreSQL.
- Refer to `Lesson 1 Demo 2` and `Lesson 1 Exercise 2`.

#### Lesson 2 - Relational Data Models

> Students will learn the fundamentals of how to do relational data modeling by focusing on normalization, denormalization, fact/dimension tables, and different schema models.

Definitions:

- Database: set of related data and the way it is organized.
- DBMS: computer system that allows users to interact with the databases and provides access to all of the data. Because of the close relationship, the term database is often used to refer to both the database and the DBMS used.

*Rule 1: The information rule*
All information in a relational database is represented explicitly at the logical level and in exactly one way – by values in tables.

- **Online Analytical Processing (OLAP)**
Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are optimized for reads.

- **Online Transactional Processing (OLTP)**
Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

The key to remember the difference between OLAP and OLTP is analytics (A) vs transactions (T). If you want to get the price of a shoe then you are using OLTP (this has very little or no aggregations). If you want to know the total stock of shoes a particular store sold, then this requires using OLAP (since this will require aggregations).

Structuring the database:
- **Normalization**: To reduce redundancy and increase data integrity. The process of structuring a relational database in accordance with a series of normal forms in order to reduce data redundancy and increase data integrity. We want fewer copies and that our records are the single source of truth. The table below is not normalized.

- **Denormalization**: Must be done in read heavy workloads ato increase performance.

![](./images/8.png)

Objectives of **Normal Form**:
- To free the database from unwanted insertions, updates, and deletion dependencies. The fewer places you need to update the data, less prone to error you are...
- To reduce the need for refactoring the database as new types of data are introduced.
- To make the relational model more informative to users.
- To make the database neutral to the query statistics.

**Normal Forms**

- Normalization is a step by step process. There are more than three but not really done in production, more for academics.

**How to reach First Normal Form (1NF)**

- Atomic values: each cell contains unique and single values
- Be able to add data without altering tables (adding or removing columns)
- Separate different relations into different tables
- Keep relationships between tables together with foreign keys

**Second Normal Form (2NF)**

- Have reached 1NF
- All columns in the table must rely on the Primary Key

In the example below, the store ID is not unique and so we need two columns to get a unique record. So we break the bigger table down into two smaller ones.

![](./images/9.png)

**Third Normal Form (3NF)**

- Must be in 2nd Normal Form
- No transitive dependencies
- Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.

![](./images/10.png)
![](./images/11.png)

In the first table, we need to know `music award` + `year` to identify one `winner record of year`. And then the `lead singer` is extra info. Jon Lennon is repeated in rows 1 and 3. Then if that was updated, we would need to update in multiple locations...

**When to use 3NF**

When you want to update data, we want to be able to do in just 1 place. 

- Refer to `Lesson 2 Demo 1` and `Lesson 2 Exercise 1`.

**Denormalization**

> The process of trying to improve the read performance of a database at the expense of losing some write performance by adding redundant copies of data.

JOINS on the database allow for outstanding flexibility but are extremely slow. If you are dealing with heavy reads on your database, you may want to think about denormalizing your tables. You get your data into normalized form, and then you proceed with denormalization. So, denormalization comes after normalization.

Requires more space in the system but now space is not really a limiting factor. Denormalization is part of the data modeling process to make data more easily queried. We want to think about the queries that we are running and how we can reduce our number of JOINS even if that means duplicating data. 

Logical Design Change:
- The designer is in charge of keeping the data consistent (all copies are consistent at any time)
- Reads will be fast (select)
- Writes will be slower (insert, update, delete)

![](./images/12.png)

In summary:

- Normalization is about trying to increase data integrity by reducing the number of copies of the data. Data that needs to be added or updated will be done in as few places as possible.

- Denormalization is trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).

- Refer to `Lesson 2 Demo 2` and `Lesson 2 Exercise 2`.

Example of Denormalized Data:
As you saw in the earlier demo, this denormalized table contains a column with the Artist name that includes duplicated rows, and another column with a list of songs.

![](./images/13.png)

Example of Normalized Data:
Now for normalized data, Amanda used 3NF. You see a few changes:
1) No row contains a list of items. For e.g., the list of song has been replaced with each song having its own row in the Song table.
2) Transitive dependencies have been removed. For e.g., album ID is the PRIMARY KEY for the album year in Album Table. Similarly, each of the other tables have a unique primary key that can identify the other values in the table (e.g., song id and song name within Song table).

![](./images/14.png)
![](./images/15.png)

**Fact and Dimension Tables**

- Work together to create an organized data model
- While fact and dimension are not created differently in the DDL, they are conceptual and extremely important for the organization.
- One or more fact table(s) for each dimension table.
- Fact tables consist of the measurements, metrics or facts of a business process. Not meant to be updated in place like a dimension table would. Normally have numbers. 
- Dimension is a structure that categorizes facts and measures in order to enable users to answer business questions. Dimensions are people, products, place and time. Include textual and numerical information not used for analysis. 

Two of the most popular data mart schema for data warehouses are:
- **Star Schema**
- **Snowflake Schema**

**Star Schema** is the simplest style of data mart schema. The start schema consists of one or more fact tables referencing any number of dimension tables.

In this example, it helps to think about the Dimension tables providing the following information:

Where the product was bought? (Dim_Store table)
When the product was bought? (Dim_Date table)
What product was bought? (Dim_Product table)

The Fact table provides the metric of the business process (here Sales).

How many units of products were bought? (Fact_Sales table)
![](./images/16.png)

Why "star" schema?
- Gets its name from the physical model resembling a star shape
- a fact table is at its center
- dimension table surrounds the fact table representing the star's points.

Benefits of star schema:
- Denormalized
- Simplifies queries
- Fast aggregations

Disadvantages:
- Issues that come with denormalization 
- Data integrity
- Decrease query flexibility
- Many to many relationships -- simplified

![](./images/17.png)

**Snowflake Schema** is a logical arrangement of tables in a multidimensional database represented by centralized fact tables which are connected to multiple dimensions. A complex snowflake shape emerges when the dimensions of a snowflake schema are elaborated, having multiple levels of relationships, child tables having multiple parents.

![](./images/18.png)

The star schema is a simplified case of the snowflake schema. The star schema does no allow for one to many relationships while the snowflake schema does. The snowflake schema is more normalized that the star schema, but only in 1NF or 2NF.

![](./images/19.png)

[Medium post on the differences between Star and Snowflake Schemas](https://medium.com/@BluePi_In/deep-diving-in-the-world-of-data-warehousing-78c0d52f49a)

- Refer to `Lesson 2 Demo 3` and `Lesson 2 Exercise 3`.

![](./images/20.png)
![](./images/21.png)
![](./images/22.png)
![](./images/23.png)
![](./images/24.png)

- Refer to `Project 1`.


#### Lesson 3 - NoSQL Data Models

> Students will learn the fundamentals of data modeling or NoSQL databases, focusing on the basics of NoSQL database design, denormalization, primary keys, clustering columns, and the WHERE clause.

- NoSQL and Non-Relational are interchangeable terms
- NoSQL = Not only SQL

**When Not to Use SQL**

- Need high Availability in the data: Indicates the system is always up and there is no downtime
- Have Large Amounts of Data
- Need Linear Scalability: The need to add more nodes to the system so performance will increase linearly
- Low Latency: Shorter delay before the data is transferred once the instruction for the transfer has been received.
- Need fast reads and writes
- Apache Cassandra is an example of a NoSQL database

Here is a helpful blog that describes the different types of NoSQL databases - <https://www.xenonstack.com/blog/nosql-databases/>.

**Apache Cassandra**
- Open source
- Masterless architecture
- High availability - no single point of failure
- Linearly scalable
- Used by Uber, Netflix, Twitter, Facebook...
- Created to handle big data challenges that relational databases failed to tackle

In a distributed database, in order to have high availability you will need copies of your data. It is made up of multiple machines (horizontally scaled). Since there are copies of data to cope with eventual nodes crashing, data might not be up-to-date in all nodes - **eventual consistency**.

**Eventual Consistency:**
Over time (if no new changes are made) each copy of the data will be the same, but if there are new changes, the data may be different in different locations. The data may be inconsistent for only milliseconds. There are workarounds in place to prevent getting stale data. Or, in other words, a consistency model used in distributed computing to achieve high availability at informally guarantees that, f no new updates are made to a given data item, eventually all accesses to that item will return the last updated value.

**CAP Theorem:**
> It is impossible for a distributed data store to simultaneously provide more than two out of three guarantees of consistency, availability and partition tolerance.

**Consistency**: Every read from the database gets the latest (and correct) piece of data or an error

**Availability**: Every request is received and a response is given -- without a guarantee that the data is the latest update

**Partition Tolerance**: The system continues to work regardless of losing network connectivity between nodes

![](./images/25.png)

When there is no network failures, it is possible to achieve consistency and availability. However, if there is a network failure, you may only have consistency or availability. Apache Cassandra chooses to be highly available at the potential cost of consistency! It is a `AP` type of database.

***Commonly Asked Questions:***
- Is Eventual Consistency the opposite of what is promised by SQL database per the ACID principle?

Much has been written about how Consistency is interpreted in the ACID principle and the CAP theorem. Consistency in the ACID principle refers to the requirement that only transactions that abide by constraints and database rules are written into the database, otherwise the database keeps previous state. In other words, the data should be correct across all rows and tables. However, consistency in the CAP theorem refers to every read from the database getting the latest piece of data or an error.

- Which of these combinations is desirable for a production system - Consistency and Availability, Consistency and Partition Tolerance, or Availability and Partition Tolerance?

As the CAP Theorem Wikipedia entry says, "The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability." So there is no such thing as Consistency and Availability in a distributed database since it must always tolerate network issues. You can only have Consistency and Partition Tolerance (CP) or Availability and Partition Tolerance (AP). Remember, relational and non-relational databases do different things, and that's why most companies have both types of database systems.

- Does Cassandra meet just Availability and Partition Tolerance in the CAP theorem?

According to the CAP theorem, a database can actually only guarantee two out of the three in CAP. So supporting Availability and Partition Tolerance makes sense, since Availability and Partition Tolerance are the biggest requirements.

- If Apache Cassandra is not built for consistency, won't the analytics pipeline break?

If I am trying to do analysis, such as determining a trend over time, e.g., how many friends does John have on Twitter, and if you have one less person counted because of "eventual consistency" (the data may not be up-to-date in all locations), that's OK. In theory, that can be an issue but only if you are not constantly updating. If the pipeline pulls data from one node and it has not been updated, then you won't get it. Remember, in Apache Cassandra it is about Eventual Consistency.

**Denormalization in Apache Cassandra**

- Denormalization is not just okay -- it's a must
- Denormalization must be done for fast reads
- Apache Cassandra has been optimized for fast writes
- ALWAYS think Queries first
- One table per query is a great strategy
- Apache Cassandra does not allow for JOINs between tables

If migrating from SQL to NoSQL the data model will need to be redesigned, migration as is will not work. 3NF does not work, there are not joins! Storage isn't expensive, losing customers to low performance or outages is. Apache Cassandra requires a paradigm shift from thinking about queries in relational databases. It is 1 table per single query.

![](./images/26.png)

- I see certain downsides of this approach, since in a production application, requirements change quickly and I may need to improve my queries later. Isn't that a downside of Apache Cassandra?

In Apache Cassandra, you want to model your data to your queries, and if your business need calls for quickly changing requirements, you need to create a new table to process the data. That is a requirement of Apache Cassandra. If your business needs calls for ad-hoc queries, these are not a strength of Apache Cassandra. However keep in mind that it is easy to create a new table that will fit your new query.

- Cassandra Query Language (CQL) is the way to interact with the database and is very similar to SQL. JOINS, GROUP BY, or subqueries are not in CQL and are not supported by CQL.

- Refer to `Lesson 3 Demo 1` and `Lesson 3 Exercise 1`.

**Primary Key**

- How each row can be uniquely identified and how the data is distributed across the nodes (or servers) in our system.
- The first element of the `PRIMARY KEY` is the `PARTITION KEY` which will determine the distribution.
- The `PARTITION KEY`'s row value will be hashed (turned into a number) and stored on the node in the system that holds the range of values.
- Must be unique.
- The `PRIMARY KEY` is made up of either just the `PARTITION KEY` or may also include additional `CLUSTERING COLUMNS`.
- A Simple `PRIMARY KEY` is just one column that is also the `PARTITION KEY`. A `Composite PRIMARY KEY` is made up of more than one column and will assist in creating a unique value and in your retrieval queries.
- The `PARTITION KEY` will determine the distribution of data across the system. We want to pick a key that will evenly distribute the data. Ex: is it's state it will not be evenly distribute since different states have different population sizes.

![](./images/27.png)
![](./images/28.png)

- Which is better: Simple or Composite Primary Keys?

It depends on the data you have and the queries you will run. You may need to combine several columns in the Primary Key to make a Composite Key so that each of the rows are unique.

- Refer to `Lesson 3 Demo 2` and `Lesson 3 Exercise 2`.

**Clustering Columns:**
- The clustering column will sort the data in sorted ascending order, e.g., alphabetical order. 
- More than one clustering column can be added (or none!).
- From there the clustering columns will sort in order of how they were added to the primary key.

![](./images/29.png)
![](./images/30.png)

- How many clustering columns can we add?
You can use as many clustering columns as you would like. You cannot use the clustering columns out of order in the `SELECT` statement. You may choose to omit using a clustering column in your `SELECT` statement. That's OK. Just remember to use them in order when you are using the `SELECT` statement.

- Refer to `Lesson 3 Demo 3` and `Lesson 3 Exercise 3`.

**WHERE clause**
- Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the `WHERE` clause.
- The `PARTITION KEY` must be included in your query and any `CLUSTERING COLUMNS` can be added in order they appear in your `PRIMARY KEY`.
- Failure to include a `WHERE` clause will result in an error.

![](./images/31.png)

- `SELECT * FROM TABLE`: the where clause must be included to execute queries. It is recommended that one partition be queried at a time for performance implications. It is possible to do a `select * from table` if you add a configuration `ALLOW FILTERING` to your query. This is risky, but available if absolutely needed.

- Why do we need to use a `WHERE` statement since we are not concerned about analytics? Is it only for debugging purposes?

The WHERE statement is allowing us to do the fast reads. With Apache Cassandra, we are talking about big data -- think terabytes of data -- so we are making it fast for read purposes. Data is spread across all the nodes. By using the WHERE statement, we know which node to go to, from which node to get that data and serve it back. For example, imagine we have 10 years of data on 10 nodes or servers. So 1 year's data is on a separate node. By using the WHERE year = 1 statement we know which node to visit fast to pull the data from.

- Refer to `Lesson 3 Demo 4` and `Lesson 3 Exercise 4`.


### Section 3 - Cloud Data Warehouses

#### Lesson 1 - Intro to Data Warehouses

> Students will be able to understand the purpose, architecture, and technologies used in a data warehouse.

What is a Data Warehouse?

- In a Business perspective:
![](./images/32.png)
![](./images/33.png)
![](./images/34.png)
![](./images/35.png)
![](./images/36.png)
![](./images/37.png)

- In a Technical perspective:

> A copy of transaction data specifically structured for query and analysis.

> Is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of management's decisions.

> Is a system that retrieves and consolidates data periodically from the source systems into a dimensional and normalized data stores. It usually kee[s years of history and is queried for business intelligence or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system.

![](./images/38.png)
![](./images/39.png)
![](./images/40.png)

**Data Warehouse Goals**
- Simple to understand
- Performant
- Quality assured
- Handles new questions well
- Secure

![](./images/41.png)
![](./images/42.png)
![](./images/43.png)
![](./images/44.png)

- Refer to `Lesson 4 Exercise 1`.

**DWH Architecture**

![](./images/45.png)
![](./images/46.png)

According to Kimball's Bus Architecture, data is kept in a common dimension data model shared across different departments. It does not allow for individual department specific data modeling requirements.

![](./images/47.png)
![](./images/48.png)

Independent Data Marts are highly discouraged.

![](./images/49.png)
![](./images/50.png)

- The Enterprise Data Warehouse provides a normalized data architecture before individual departments build on it. 
- Corporate Information Factory (CIF) build on a 3NF normalized database and then allow for documented data denormalization for Data Marts. 
- Corporate Information Factory (CIF) build on a 3NF normalized database and then allow for documented data denormalization for Data Marts.

![](./images/51.png)
![](./images/52.png)
![](./images/53.png)
![](./images/54.png)
![](./images/55.png)
![](./images/56.png)
![](./images/57.png)

**DWH Technologies**

![](./images/58.png)

- OLAP cubes is a very convenient way of slicing, dicing and drilling down.

- How do serve these OLAP CUBES?
1. Approach 1: Pre-aggregate the OLAP cubes and saves them on a special purpose non-relational database (**MOLAP**)
2. Approach 2: Compute the OLAP cubes on the fly from the existing relational databases where the dimensioanal model redis (**ROLAP**)

### Lesson 2 - Introduction to Cloud Computing and AWS

> Welcome to this lesson on Introduction to the Cloud and AWS. You'll learn about the cloud infrastructure ecosystem and understand how to use essential tools for computing, storage, and analytics through one of the biggest providers of cloud computing, Amazon Web Services.

What Is **Cloud Computing**?
Cloud computing: the practice of using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.

The arrival of cloud computing completely changed the way we deploy our technology, providing powerful access to instant and scalable computing power to enterprises, startups, and developers alike. Whether you need servers to host a web application, reliable storage for your data, or machines to train machine learning models, it's easy to see the advantage of relying on the cloud rather than utilizing your personal computer or local servers.

For one, you no longer have to invest in lots of hardware upfront. No need to worry about whether you are paying for more than you'll need or what to do if you need to scale a lot more later on. Cloud computing makes this as easy and clicking a few buttons to scale your resources up or down.

It's significantly faster provisioning the resources you need through the cloud versus the time it would take to gather and build up the hardware you'd need to provide the same support. This allows you and your team, or company, to develop and experiment at a much faster rate.

Lastly, you can provide efficient access to your applications around the world by spreading your deployments to multiple regions.

**Amazon Web Services**
Amazon Web Services is one of the largest providers in the cloud computing industry, with over 140 services in compute, storage, databases, networking, developer tools, security, and more. In this lesson, we'll learn about a few essential tools and services in AWS and practice using them. These services can be accessed in three different ways: the AWS Management Console, the Command Line Interface (CLI), or Software Development Kits (SDKs), which can be used in combination.

We'll start with the AWS Management Console, which is the web user interface. The AWS CLI is a useful way to control and automate your services with code, and SDKs allow you to easily integrate services with your applications through APIs built around specific languages and platforms.

**Using AWS Management Console**
- Create an `IAM role` to attach to `Redshift cluster` to enable your cluster to load data from Amazon S3 buckets. Read more about IAM roles and Redshift [here](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html).
- Create `security group` to be used to authorize access to your Redshift cluster.
- Launch a Redshift cluster.
- Create an `IAM User` to be used to access Redshift cluster with `AmazonRedshiftFullAccess` and `AmazonS3ReadOnlyAccess`. Download CSV with credentials.
- Delete cluster to avoid unexpected costs.
- Create an S3 bucket and upload file to it.
- Create a PostgreSQL DB Instance using RDS.

**Implementing DWH on AWS**

> Students will be able to implement a data warehouse on AWS including scalable storage , ETL strategies, and design and query optimization. 

![](./images/58.png)
![](./images/59.png)
![](./images/60.png)
![](./images/61.png)
![](./images/62.png)
![](./images/63.png)
![](./images/64.png)
![](./images/65.png)
![](./images/66.png)
![](./images/67.png)
![](./images/68.png)
![](./images/69.png)
![](./images/70.png)
![](./images/71.png)
![](./images/72.png)

- The total number of nodes in a Redshift cluster is equal to: The number of AWS EC2 instances used in the cluster.
- Each slice in a Redshift cluster is: At least 1 CPU with dedicated storage and memory for the slice.
- If we have a Redshift cluster with 4 nodes, each containing 8 slices, i.e. the cluster collectively offers 32 slices. What is the maximum number of partitions per table? 32 partitions! The total number of slices in a cluster is our unit of parallelism and it is equal to the sum of all slices on the cluster.

![](./images/73.png)
![](./images/74.png)
![](./images/75.png)
![](./images/76.png)

- ETL Servers talk to different databases and need to store data as it moves it from one place to the next. So they need to have large storage capacity!

![](./images/77.png)

- We store all the data in S3 buckets, we do not need storage on the EC2 machine. S3 offers a very reliable, scalable and worry-free storage solution, but it only offers storage not processing power.

![](./images/78.png)

- We can pre-aggregate data with OLAP cubes to feed BI apps and upload to S3. Redshift can also feed the BI apps directly though.
- We need the staging bucket since we will most likely transform the data before inserting it into the DHW.

![](./images/79.png)

- Bulk insertion in a SQL database is faster than doing it record by record.

- Why do we split a table into multiple files before ingestion? Because this way we can execute multiple simultaneous COPY commands. Each Redshift slice will act as a separate worker and will use ingest the split of a file in parallel, so the process will complete much faster.

![](./images/80.png)
![](./images/81.png)
![](./images/82.png)
![](./images/83.png)
![](./images/84.png)

- Usually you'll want to use S3 as a staging area, but for very small data, you might want to copy it directly from the EC2 machine.

![](./images/85.png)
![](./images/86.png)
![](./images/87.png)
![](./images/88.png)
![](./images/89.png)
![](./images/90.png)

- Which of the following are advantages of Infrastructure-as-Code over creating infrastructure by clicking-around? Sharing, Reproducibility, Multiple Deployments & Maintainability are all advantages of IaC. One can track all the steps with others easily. One can be sure that no steps are forgotten. One can create a test environment identical to the production environment. If a change is needed, one can keep track of the changes by comparing the code.

![](./images/91.png)
![](./images/92.png)
![](./images/93.png)
![](./images/94.png)
![](./images/95.png)
![](./images/96.png)
![](./images/97.png)

- Joining 2 tables distributed using an EVEN strategy is slow because records will have to be shuffled for putting together the JOIN result. Yes, because e.g. a given key (say key=2532) of table 1 will not be on the same slice as the corresponding record in table 2, so record will be copied (shuffled) between slices on different nodes, which results in slow performance.

![](./images/98.png)
![](./images/99.png)

Note: In general, dimension tables are small compared to fact tables.

![](./images/100.png)
![](./images/101.png)
![](./images/102.png)
![](./images/103.png)
![](./images/104.png)
![](./images/105.png)
![](./images/106.png)
![](./images/107.png)
![](./images/108.png)

### Section 4 - Data Lakes with Spark

#### Lesson 1 - The Power of Spark

Spark is currently one of the most popular tools for big data analytics. You might have heard of other tools such as Hadoop. Hadoop is a slightly older technology although still in use by some companies. Spark is generally faster than Hadoop, which is why Spark has become more popular over the last few years.

There are many other big data tools and systems, each with its own use case. For example, there are database system like Apache Cassandra and SQL query engines like Presto. But Spark is still one of the most popular tools for analyzing large data sets.

Here is an outline of the topics we are covering in this lesson:

- What is big data?
- Review of the hardware behind big data
- Introduction to distributed systems
- Brief history of Spark and big data
- Common Spark use cases
- Other technologies in the big data ecosystem

![](./images/109.png)

**The Numbers Everyone Should Know**
- How long does it take for your CPU to add two numbers?
- How quickly can you look up an appointment if your calendar is already chached in your computer's memory?
- How many seconds does it take to load up your favourite song from your laptop's SSD storage?
- How much data can you download from Netflix in a minute?

![](./images/110.png)

In the next few videos, you'll learn about four key hardware components. Understanding these components helps determine whether you are working on a "big data" problem or if it's easier to analyze the data locally on your own computer.

**CPU (Central Processing Unit)**
The CPU is the "brain" of the computer. Every process on your computer is eventually handled by your CPU. This includes calculations and also instructions for the other components of the compute.

**Memory (RAM)**
When your program runs, data gets temporarily stored in memory before getting sent to the CPU. Memory is ephemeral storage - when your computer shuts down, the data in the memory is lost.

**Storage (SSD or Magnetic Disk)**
Storage is used for keeping data over long periods of time. When a program runs, the CPU will direct the memory to temporarily load data from long-term storage.

**Network (LAN or the Internet)**
Network is the gateway for anything that you need that isn't stored on your computer. The network could connect to other computers in the same room (a Local Area Network) or to a computer on the other side of the world, connected over the internet.

Other Numbers to Know?
You may have noticed a few other numbers involving the L1 and L2 Cache, mutex locking, and branch mispredicts. While these concepts are important for a detailed understanding of what's going on inside your computer, you don't need to worry about them for this course.

![](./images/111.png)

CPU operations are fastest. Operations in memory (RAM) are the second fastest. Then comes hard disk storage and finally transferring data across a network. Keep these relative speeds in mind. They'll help you understand the constraints when working with big data.

The CPU is the brains of a computer. The CPU has a few different functions including directing other components of a computer as well as running mathematical calculations. The CPU can also store small amounts of data inside itself in what are called registers. These registers hold data that the CPU is working with at the moment.

For example, say you write a program that reads in a 40 MB data file and then analyzes the file. When you execute the code, the instructions are loaded into the CPU. The CPU then instructs the computer to take the 40 MB from disk and store the data in memory (RAM). If you want to sum a column of data, then the CPU will essentially take two numbers at a time and sum them together. The accumulation of the sum needs to be stored somewhere while the CPU grabs the next number.

This cumulative sum will be stored in a register. The registers make computations more efficient: the registers avoid having to send data unnecessarily back and forth between memory (RAM) and the CPU.

![](./images/112.png)
![](./images/113.png)

- Ex: No problem for a single machine to process one day of worldwide tweets.

![](./images/114.png)
![](./images/115.png)
