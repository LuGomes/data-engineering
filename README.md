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