# SSMS Tips & Reference Sheet

## Getting Started

* **Connect to a server:**
  When opening SSMS, you’ll be prompted to connect to a SQL Server instance.

  * *Server type:* Database Engine
  * *Authentication:* Windows or SQL Server Authentication
  * *Server name:* e.g. `localhost`, `.\SQLEXPRESS`, or a remote host.

* **Query windows:**
  Use the “New Query” button to open a SQL editor connected to your selected database.
  You can check or change which database you’re connected to using the dropdown in the toolbar.

---

### Common Shortcuts

|Action|Shortcut|
|---|---|
|Execute current query|**F5** or **Ctrl + E**|
|Comment selected lines|**Ctrl + K, Ctrl + C**|
|Uncomment lines|**Ctrl + K, Ctrl + U**|
|Format SQL (if installed)| **Ctrl + K, Ctrl + D**|
|Switch database|Use `USE [database_name];`|
|Display object list|**F8** opens the Object Explorer|
|View results in grid/text|`Ctrl + D` (grid) or `Ctrl + T` (text)|

---

### Useful Built-In Features

|Feature|Description|
|---|---|
|**Object Explorer**|View all databases, tables, views, stored procedures, and functions.|
|**Query Designer**|Visual interface for building SELECT statements.|
|**Results Pane**|Displays query output — can switch between grid, text, or file output.|
|**Messages Tab**|Displays success/failure messages and execution time.|
|**Activity Monitor**|View current server activity, performance, and locks (right-click the server → *Activity Monitor*).|

---

### Checking Database Objects

In T-SQL, instead of `SHOW TABLES;` or `DESCRIBE table;` (used in MySQL), use:

```sql
-- List all tables in the current database
SELECT * FROM INFORMATION_SCHEMA.TABLES;

-- Get column details for a specific table
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'customers';
```

Or use SQL Server’s system stored procedures:

```sql
EXEC sp_help 'customers';
```

---

### INFORMATION_SCHEMA vs TABLE SCHEMA

|Concept| Description|
|---|---|
|**Table Schema**|The *namespace* a table belongs to within a database. By default, most user-created tables belong to the `dbo` schema. You can think of it as a folder name within the database. <br><br>**Example:**<br>`CREATE TABLE sales.customers (...);`<br>Here, `sales` is the *table schema*, and `customers` is the table name.|
|**INFORMATION_SCHEMA**|A *system view* that provides metadata about all database objects (tables, columns, constraints, etc.) in a standardized SQL format. It’s part of the ANSI SQL standard, so it works across many RDBMSs. <br><br>**Example views include:**<br>- `INFORMATION_SCHEMA.TABLES` — lists all tables<br>- `INFORMATION_SCHEMA.COLUMNS` — details about columns<br>- `INFORMATION_SCHEMA.KEY_COLUMN_USAGE` — shows primary/foreign keys|

**Analogy:**
Think of **INFORMATION_SCHEMA** as a *directory of blueprints* for the database — it describes your tables, not the data inside them.
Meanwhile, a **table schema (like dbo)** is the *container* or *namespace* that actually holds those tables.

---

### Managing Databases and Tables

|Action|T-SQL Command|
|---|---|
|Create a new database|`CREATE DATABASE myDB;`|
|Switch to it|`USE myDB;`|
|Create a table|`CREATE TABLE dbo.customers (...);`|
|Delete a table|`DROP TABLE dbo.customers;`|
|View all databases|`SELECT name FROM sys.databases;`|
|Rename a table|`EXEC sp_rename 'old_name', 'new_name';`|

---

### Pro Tips

* Always **prefix tables with schema name** (e.g., `dbo.customers`) — improves clarity and performance in larger databases.
* To **explore table relationships** visually, right-click the database → *Database Diagrams* → *New Diagram*.
* You can **script** almost any action from the GUI: right-click an object → *Script As → CREATE / ALTER / DROP / SELECT*.
* When writing multi-line queries, use **GO** to separate batches.

  ```sql
  USE myDB;
  GO
  CREATE TABLE dbo.example (...);
  GO
  ```

---

### Example: Inspecting a Table’s Schema

```sql
-- 1. See where the table lives and who owns it
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'orders';

-- 2. See column details
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'orders';
```

---

Would you like me to format this sheet into a **downloadable .md file** so you can drop it straight into your course materials?
