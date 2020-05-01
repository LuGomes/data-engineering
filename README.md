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
