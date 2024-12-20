# Intro to Databases

Pretty much every organisation that holds data will have it in a database which makes it easier to store, manage, and retrieve the data. 
There are various different database options available, which are often tailored to specific use cases, however they all fit into one of two categories, SQL and NoSQL.

## Relational Databases (SQL)
### RDBMS

The software that lets you create, manage, and query databases, is called a **relational database management system**. Some popular ones include:
- MySQL
- PostgreSQL
- Microsoft SQL Server

### Practical 1

- Install MySQL
- snapshot VM

### SQL Databases

Structured Query Language (SQL) is a database type which was developed in the 70’s, based on theoretical relational data models proposed in the 60’s. SQL databases are also known as relational databases.
SQL databases store data in tables which are defined by a schema. Each data item entered into the table must adhere to this schema.
You can create multiple tables, and then create relationships between them based on data items they have in common.

We're going to install a database engine (an RDBMS) on our Linux In a momr, but when done we need to create a database, in which we can create our tables to store our data. 

To create a database use the following SQL command.

```sql
CREATE DATABASE test_db;
```

We can then verify it was created with.

```sql
SHOW DATABASES;
```

Once created we need to move into that database so that we can start working with it.

```sql
USE test_db;
```

We can also delete databases with the DROP keyword.

```sql
DROP DATABASE test_db;
```

CREATE and DROP can also be used for tables, which we'll look at shortly. 

### The SQL Language

Although you can interact with SQL databases via a GUI, SQL was developed at a time when GUI’s were not common, and much like Linux, maximum compatibility is still achieved through the use of the standardised command set and syntax.

Many of the different types of SQL databases have their own additional features, such as supporting unique data types, or in some cases restrictions, such as naming conventions, but they should all support the standard SQL features and commands.

The SQL commands can be divided into three groups based on the type of functionality they provide:
- DDL - used to define the structure of the database and its objects such as tables, schemas, and indexes.
- DML - used to manipulate data within the database
- DQL - commands to retrieve data from the database
- DCL - used to manage access to the database by granting or revoking permissions.
- TCL - commands to manage transactions within a database to ensure data integrity.

SQL commands have simple syntax and conventions, compared to say Python or Bash. A basic SQL query looks like this - *Don't worry about what it does right now, we'll come back to it shortly*:

```sql
SELECT * FROM customers WHERE Name = “Company A”;
```

Commonly they’re split over multiple lines for readability. SQL doesn’t care about newlines, it looks for the semi-colon (;) to end the statement - missing the semi-colon is a common mistake, if your terminal is showing this prompt `->` it often means you missed the `;`.

```sql
SELECT * FROM customers 
WHERE Name = “Company A”;
```

One convention is that SQL keywords are capitalised, therefore for easy readability tables and fields are usually in lower case. **NOTE: SQL keywords are not case-sensitive, but database, table, and field names are.**

### SQL Tables

A database will typically contain multiple tables, but exactly which ones is up to you and your organisation’s needs. 

A common example when learning is to model a simple business which needs a customer_table, products_table, and an orders_table.

Tables in SQL are comprised of Fields (columns) and Records (rows), each record is an new entry in the database, and the fields are the data items captured for each record.

Every record in the table needs a unique identifier, known as a ‘Primary Key’, since two entries might have the same name.

When one table has a field for another table’s Primary Key, such as an Orders table referencing a Customer_ID number when they make a purchase, we call this a Foreign Key. 

Linking Primary and Foreign keys is how we create relationships between tables.

*Instructor prompt: WB*

### SQL Schema

Here is an example of creating a basic employee table and schema:

```sql
CREATE TABLE customers (
	customer_ID INT NOT NULL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	age INT UNSIGNED NOT NULL
);
```

Like with the database, we can verify our table was created with `SHOW tables;`, but to ensure that all of our data types and additional options are configured correctly we can see a more detailed overview with

```sql
DESCRIBE customers;
```

We’re only using two data types, INTs and VARCHARS, but many more area available. However, there are several points worth reviewing…

### SQL Data Types

Although some of the different SQL databases have been developed to support niche data types and features, most standard data types are supported by all:
- INT = whole numbers, use UNSIGNED to restrict to positive numbers only.
- DECIMAL = decimal numbers to a defined precision e.g. DECIMAL(8, 2) stores up to 8 digits, with 2 after the decimal point. 
- CHAR(number) = a fixed length string
- VARCHAR(number) = a string up to the specified length
- DATE, TIME, DATETIME = yy-mm-dd, hh:mm:ss, YYYY-MM-DD hh:mm:ss
- BOOLEAN = true/false
And many others…

### Practical 2

- Practice creating and dropping databases and tables.
- Try to use CREATE, DROP, SHOW, USE, and DESCRIBE.

### Working with Data

Adding records to the database can be done in a number of ways. We are going to use standard SQL commands through the CLI, but this would not be suitable for a non-technical user.

Commonly a GUI can be created which translates user input into the appropriate SQL statements in the back-end, allowing these users to add and query data in a user-friendly environment.

Data can also be imported and exported in bulk using a variety of file types, a common option being CSV files.

### Inserting Records

Adding records into a table can be done with the INSERT statement as follows:

```sql
INSERT INTO customers (customer_ID, first_name, last_name, age) 
VALUES (1, 'Alice', 'Smith', 33);
```

As we're just learning, it's good practice to verfiy your record, you can do so by running a simple SELECT statement.

```sql
SELECT * FROM customers;
```

We'll come back to the SELECT statement shortly.

We'll look at some variations which can add multiple records at once through the CLI, but you should probably stick to one at a time for now to build familarity with the logic.

### Updating Records

To make changes to existing records use the UPDATE statement.

```sql
UPDATE customers
SET Age = 31
WHERE customer_ID = 1;
```

Notice the WHERE clause, this allows you to filter the records you retrieve from the database, in this case to make a simple update. But this is the key to retrieving with the SELECT statement, and gaining insights into your data. 

### Practical 3

- Create customers, and products tables with appropriate fields defined.
- Insert records into each table.
- Verify your records with `SELECT * FROM [table]`
- Update records.

### Selecting Records

Databases allow you to store, manage, and retrieve your data. Retrieval is about providing access to your data quickly and efficiently, for example looking up a customer’s records when then call in for support. 

```sql
SELECT *
FROM customers
WHERE customer_ID = 1;
```

The above example uses the wildcard `*` to return all fields, but you can also specify the specific fields you want.

```sql
SELECT first_name, last_name
FROM customers
WHERE customer_ID = 3;
```

Quick retrieval is one of the primary uses for a database, commonly GUI based applications which are easy for non-technical users to navigate and interact with, have databases in the back-end, such as a CRM system which looks up customer information when they call in for support; Or a web-based storefront, in which all of the product information is recalled from a database as the customer navigates the different items.

### Practical 4

- Add several records and practice SELECT statements against created tables

### More SELECT statements

#### Comparison Operators

Similar to Python, Bash, and many other environments, we can use comparison operators in our queries to further refine them, **but only against numeric values**.

```sql
SELECT first_name, last_name 
FROM customers 
WHERE age > 30;
```

The following comparison operators can be used

|Comparison         |Syntax |
|-------------------|-------|
|Equal              |=      |
|Not equal          |= or !=|
|Greater            |>      |
|Greater or equal   |>=     |
|Less               |<      |
|Less or equal      |<=     |

#### String Patterns

We do have the ability to match patterns in strings, but we use the LIKE or NOT LIKE clauses in our SQL statements.  

|Pattern                    |Syntax        |
|---------------------------|--------------|
|Strings starting with 'abc'|'abc%'        |
|Strings ending with 'abc'  |'%abc'        |
|'abc' within the string    |'%abc%'       |
|Exactly X characters long  |'___' (3 here)|
|_ can be any character     |'a_c'         |

Here's an example of the syntax.

```sql
SELECT first_name, last_name 
FROM customers 
WHERE first_name LIKE 'Al%';
```

The SELECT statement also allows you to analyse your data to identify patterns, trends, and answer questions. 

You can write queries to identify not only the best selling products, and the biggest spending customers, but also go deeper. What about the best selling products by geography, time of year, or both? Who are the biggest spending customers by age? Or any other summaries, or insights you can think of.

This extra insight might inform decisions for marketing teams, promotion planning, inventory purchasing, future investment, and so on…

#### Sorting Results

The ORDER BY clause allows you to specify the order your returned records will be displayed.

```sql
SELECT * FROM customers WHERE age <10 ORDER BY first_name;
```

You can provide multiple sort fields by seperating them with a comma.

```sql
SELECT * FROM customers WHERE age <10 ORDER BY last_name, first_name;
```

#### Deleting Records

The query syntax you're becoming familiar with can also be used to delete individual or multiple records as needed.

```sql
DELETE FROM customers WHERE first_name LIKE 'Alice';
```

### Practical 5

- Practice SELECT statements using comparison operators and pattern matching clauses.
- Practice using ORDER BY to sort your output, and try DELETING records.

### Multiple Tables

#### Create the Tables

Most databases will require several tables, because for example, the customer table is not suitable for storing data related to the products you have in your inventory. So customers and products will be separate tables, with different schemas according to the type of data to be stored.

We've already made multiple tables, but so far they aren't *related* to each other. Let's change that.

Ideally when one table references another it should reference the target table’s Primary Key, and we define the field in the new table as a FOREIGN key.

Hopefully your CREATE TABLE statements look something like the above example.

```sql
CREATE TABLE customers (
	customer_ID INT NOT NULL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	age INT UNSIGNED NOT NULL
);

CREATE TABLE products (
    product_id INT NOT NULL PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2)
);
```
Some tables are populated with data from others, our Orders table might take data from customers and products tables to make a new entry.

Now we're going to create an orders table which references both customers and products by creating foreign.

```sql
CREATE TABLE orders (
    order_id INT NOT NULL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    order_quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**The FOREIGN key and the PRIMARY key it references should contain the same data type and attributes or you'll likely get an error.**

#### Add some Records

Lets add some data to the tables. We'll also update our syntax to add multiple records at once. 

*It is recommended that you copy the following examples to a text editor and extend them so you have more data to work with before running them in MySQL*

```sql
-- Insert records into the customers table
INSERT INTO customers (customer_id, first_name, last_name, age)
VALUES
    (1, 'Alice', 'Smith', 33),
    (2, 'Alan', 'Jones', 28),
    (3, 'Noche', 'Snead', 3);

-- Insert records into the products table
INSERT INTO products (product_id, product_name, product_price)
VALUES
    (101, 'Ryzen 7 Laptop', 1299.99),
    (102, 'iPhone 14', 799.99),
    (103, '27" Monitor', 199.99);

-- Insert records into the orders table
INSERT INTO orders (order_id, customer_id, product_id, order_date, order_quantity)
VALUES
    (201, 1, 101, '2023-11-22', 2),
    (202, 2, 102, '2023-11-23', 1),
    (203, 3, 103, '2023-11-24', 3);
```

### Practical 6

- Make customers, products, and orders tables, add records to them, ensure you can query the individual tables.

#### Query Multiple Tables

Now we have records in each table, and two of the fields in the orders table reference unique fields (i.e. primary keys) in neighbouring tables.

We've already retrieved data from individual tables, and we can view orders from the orders table in the same way. With this table structure and primary/foreign key relationships, we can create more complex SELECT statements to retrieve data from related tables together.

For example, in our companies, let's say completed orders need to go to the Despatch Team for packing and postage. They look at the orders table, and it tells them what products to pick and package, *but where do they send it*? 

One option could be to duplicate the customer details from the customer table to the orders table when they place an order. 

*Question:* Why would this not be ideal?

*Answer:* The key reasons are:
- Data duplication is inefficient and wastes space on disk.
- If the data changes it needs to be changed in multiple locations. If the data doesn't match in different locations how would you know which one is accurate?

It would be better to retrieve the current customer contact details from the most up to date source, i.e. the customer table. We can do this because there is a relationship between the customer and orders tables in our *relational database*.

The following SQL statement will retrieve the customer's first and last name for a particular record in the orders table, even though this data is not stored in the orders table. 

```sql
SELECT customers.first_name, customers.last_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_id = 201;
```

### Joins

JOIN operations combine rows from two or more tables based on a related column. In our example both tables share the customer_id field, so the above query:
1. Starts with the orders table and finds the record with order_id 201.
2. It then uses the customer_id from that record to find the corresponding record in the customers table.
3. Finally, it selects the first_name and last_name from the appropriate record, and returns them as the result.

### Aliases

Review the previous SQL statement again, notice how many times the words *customer* and *orders* are used? It's not unusual for SQL statements to become tricky for humans to read accurately, especially as you start to have many similarly named tables, and you spend 8 hours per day staring at them (if you pursue a DB Admin career path)!

Aliases allow you to define a more convenient or readable name for your tables which can be used elsewhere in your statements.

```sql
SELECT c.first_name, c.last_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_id = 201;
```

### Practical 7

- Experiment with the above syntax to create queries against your records using the join statement.

### Join Types

There are three common types of joins:

- INNER - An *Inner* join returns results from both tables which match the query condition. Our example above is an Inner join, using JOIN or INNER JOIN will both create this type of query.

- FULL (OUTER) - A Full or Outer join returns results from both tables, even where results from one table doesn't match the condition. E.g.

|Student    |Course |Score  |
|-----------|------ |-------|
|Ant        |AWS    |Null   |
|Jess       |AWS    |90     |
|Richard    |AWS    |92     |
|Ant        |AZ     |89     |
|Jess       |AZ     |Null   |
|Richard    |AZ     |93     |

Let's say we wanted to know the exam scores for three students for the AWS and AZ exams. With an Inner Join we would only get results for Jess because she has done both tests. With an Outer Join we can retrieve results with a NULL value.

- LEFT (OUTER) JOIN - Behaves like the Full Join, but it can only retrieve *none-matching* records from the left table, the table on the right's records must match the query condition.

- RIGHT (OUTER) JOIN - As above, but the table on the right can return unmatched records, and the left must meet the query.

<img src="img/joins.jpg" width="600" />

### Transactions

Another key feature of SQL databases is support for transactions. 
A transaction is a sequence of operations performed as a single logical unit of work.

To understand the concept, consider most common transactions we rely upon each day - electronic payments. Money needs to be deducted from one account, and deposited in another - if either step fails, they should both fail, and be rolled back.

Transactions must adhere to the following ACID properties:
- Atomicity: Ensures that all operations within a transaction are completed successfully. If any operation fails, the entire transaction is rolled back.
- Consistency: Guarantees that a transaction transforms the database from one valid state to another.
- Isolation: Ensures that concurrent transactions do not interfere with each other.
- Durability: Ensures that once a transaction is committed, its changes are permanently stored.

**Don’t worry about the commands or syntax for transactions, at our level just appreciate that these types of operations are traditionally one of the key features, and benefits of SQL databases.**

### Practical Challenge

- Model a company. Feel free to use the example statements from the lesson as a starting point, but they're very generic. Build them out with more fields that are tailored to your company's needs. 

    Some examples of how you might build the DB out include:
    - Add an employees table, and a field to the orders table identifying which employee made the sale.
    - Add fields to the products table to better model a company, e.g. quantity of each item in stock, item categories, colour options, sizes, etc.
    - Expand the customers table with more fields, and create queries which will generate shipping labels. 

    Anything else you can think of.