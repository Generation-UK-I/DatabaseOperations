# MySQL vs SQL Server (T-SQL)

## Comparison Sheet

|Concept / Task|MySQL Syntax|SQL Server (T-SQL) Equivalent|Notes|
|---|---|---|---|
|Create a database|CREATE DATABASE shop;|CREATE DATABASE shop;|Identical syntax.|
|Use a database|USE shop;|USE shop;|Identical syntax.|
|Create a table|sql CREATE TABLE products ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP )|sql CREATE TABLE products ( id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), created_at DATETIME DEFAULT GETDATE() );|- AUTO_INCREMENT → IDENTITY(1,1) / TIMESTAMP DEFAULT CURRENT_TIMESTAMP → DATETIME DEFAULT GETDATE()|
|List tables|SHOW TABLES;|SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;|SHOW not supported in SQL Server.|
|Rename table|RENAME TABLE old TO new;|EXEC sp_rename 'old', 'new';|SQL Server uses sp_rename.|
|Drop table|DROP TABLE products;|DROP TABLE products;|Identical.|
|Add a column|ALTER TABLE products ADD stock INT;|ALTER TABLE products ADD stock INT;|Identical.|
|Rename a column|ALTER TABLE products RENAME COLUMN price TO cost;|EXEC sp_rename 'products.price', 'cost', 'COLUMN';|Different syntax.|
|Modify column type|ALTER TABLE products MODIFY price DECIMAL(12,2);|ALTER TABLE products ALTER COLUMN price DECIMAL(12,2);|Keyword MODIFY → ALTER COLUMN.|
|Insert row|INSERT INTO products (name, price) VALUES ('Coffee', 2.50);|INSERT INTO products (name, price) VALUES ('Coffee', 2.50);|Identical.|
|Select rows|SELECT * FROM products;|SELECT * FROM products;|Identical.|
|Limit results|SELECT * FROM products LIMIT 5;|SELECT TOP 5 * FROM products;|LIMIT → TOP n.|
|Auto-increment primary key|id INT AUTO_INCREMENT PRIMARY KEY|id INT IDENTITY(1,1) PRIMARY KEY|IDENTITY(seed, increment) replaces AUTO_INCREMENT.|
|Default timestamp|TIMESTAMP DEFAULT CURRENT_TIMESTAMP|DATETIME DEFAULT GETDATE()|SQL Server uses GETDATE() or SYSDATETIME().|
|Boolean column|is_active BOOLEAN|is_active BIT|SQL Server uses BIT (0 = False, 1 = True).|
|String column|VARCHAR(255)|VARCHAR(255)|Same.|
|Text column|TEXT|VARCHAR(MAX) or TEXT (deprecated)|Use VARCHAR(MAX) in SQL Server.|
|Foreign key|sql CREATE TABLE orders ( id INT AUTO_INCREMENT PRIMARY KEY, product_id INT, FOREIGN KEY (product_id) REFERENCES products(id) );|sql CREATE TABLE orders ( id INT IDENTITY(1,1) PRIMARY KEY, product_id INT, FOREIGN KEY (product_id) REFERENCES products(id) );|Almost identical.|
|Check constraint|CHECK (price > 0)|CHECK (price > 0)|Same syntax.|
|Default value|DEFAULT 'N/A'|DEFAULT 'N/A'|Same syntax.|
|Comments|`--` Single line or `/* multi-line */`|`--` Single line or `/* multi-line */`|Same syntax.|
|Engine type|ENGINE=InnoDB;|(Not used)|SQL Server uses only its internal storage engine.|
|Show version|SELECT VERSION();|SELECT @@VERSION;|Different function names.|

### Key Differences Summary

|Category|Main Difference|
|---|---|
|Auto-increment|MySQL: `AUTO_INCREMENT` → SQL Server: `IDENTITY(1,1)`|
|Functions|MySQL uses `NOW()`, SQL Server uses `GETDATE()` or `SYSDATETIME()`|
|Result limits|MySQL: `LIMIT n` → SQL Server: `TOP n` (or OFFSET...FETCH)|
|Booleans|MySQL: `BOOLEAN` → SQL Server: `BIT`|
|Date/time types|MySQL: `TIMESTAMP`, `DATETIME` → SQL Server: `DATETIME`, `DATETIME2`|
|Renaming objects|MySQL: `RENAME TABLE`, `RENAME COLUMN` → SQL Server: `sp_rename`|
|Engines & collations|MySQL supports multiple engines (`InnoDB`, `MyISAM`, etc.) → SQL Server uses one engine but multiple collations.|

## The `EXEC` Command

The `EXEC` (short for `EXECUTE`) keyword is used to run a stored procedure, dynamic SQL command, or system stored procedure in Microsoft SQL Server.

It’s essentially SQL Server’s way of saying:

>“Run this stored procedure or this block of code right now.”

### Main Uses of `EXEC`

|Use Case|Example|Explanation|
|---|---|---|
|Run a stored procedure|`EXEC sp_help 'products';`|Executes a built-in or user-defined stored procedure. Here it shows info about the table products.|
|Run a user-defined stored procedure with parameters|`EXEC GetOrdersByCustomer @CustomerID = 5;`|Runs your own stored procedure and passes parameters.|
|Run dynamic SQL (a query built as a string)|`sql DECLARE @sql NVARCHAR(200); SET @sql = 'SELECT * FROM products WHERE price > 10'; EXEC(@sql);`|Executes a SQL command stored in a string. Useful when table names or conditions are dynamic.|
|Rename objects or view metadata (system procedures)|`EXEC sp_rename 'old_table', 'new_table';`|Uses system stored procedures (all starting with sp_).|
|Execute another database’s procedure|`EXEC OtherDatabase.dbo.usp_Example;`|Runs a procedure in another database.|
|Capture return values|`sql DECLARE @return_code INT; EXEC @return_code = MyProcedure; SELECT @return_code;`|Gets the integer return code from a stored procedure.|

### Dynamic SQL

Sometimes you can’t use normal SQL when, for example, a table name is stored in a variable. `EXEC` (or `sp_executesql`) solves that:

```sql
DECLARE @sql NVARCHAR(MAX) = 'SELECT * FROM products WHERE price > @price';
EXEC sp_executesql @sql, N'@price DECIMAL(5,2)', @price = 10.00;
```

Use `sp_executesql` for dynamic SQL — it supports parameters safely (helps prevent SQL injection).

#### Difference from MySQL

|Concept|MySQL|SQL Server|
|---|---|---|
|Run stored procedure|`CALL procedure_name();`|`EXEC procedure_name;`|
|Run dynamic SQL|`PREPARE stmt FROM ...; EXECUTE stmt;`|`EXEC(@sql) or sp_executesql`|
|Rename table, show info|`RENAME TABLE, SHOW TABLES`|`EXEC sp_rename, EXEC sp_help`|

In brief:

>`EXEC` in T-SQL = `CALL` + `EXECUTE` + `PREPARE` rolled into one — it’s how you run procedural code, not just static queries.

### Stored Procedures

`sp_help` and `sp_rename` are built-in stored procedures provided by SQL Server itself.

They’re part of the “system stored procedures” that start with `sp_` (short for stored procedure), and they’re built into the master database but accessible from any database.

These are incredibly useful for inspecting, managing, and maintaining databases without writing long T-SQL queries.

#### Common Built-in `sp_` System Stored Procedures

|Procedure|Purpose|Example Usage|Notes / Output|
|---|---|---|---|
|`sp_help`|Describes an object (table, view, etc.)|`EXEC sp_help 'products';`|Shows columns, types, indexes, constraints, etc.|
|`sp_helpdb`|Shows info about all databases or one database|`EXEC sp_helpdb; EXEC sp_helpdb 'MyDatabase';`|Size, owner, status, creation date, etc.|
|`sp_helptext`|Displays the source code of a view, trigger, or stored procedure|`EXEC sp_helptext 'MyProcedure';`|Useful for reviewing procedure or view definitions.|
|`sp_columns`|Lists columns of a table or view|`EXEC sp_columns 'products';`|Returns name, type, size, and nullability.|
|`sp_rename`|Renames tables, columns, or other objects|`EXEC sp_rename 'products.price', 'cost', 'COLUMN';`|Use carefully — can break dependencies.|
|`sp_databases`|Lists all databases on the server|`EXEC sp_databases;`|Similar to `SELECT name FROM sys.databases;`.|
|`sp_tables`|Lists tables in the current database|`EXEC sp_tables;`|Includes tables, views, and system tables.|
|`sp_stored_procedures`|Lists all stored procedures|`EXEC sp_stored_procedures;`||
|`sp_who`|Shows current connected users/processes|`EXEC sp_who;`|Basic session info.|
|`sp_who2` (undocumented but popular)|More detailed version of `sp_who`|`EXEC sp_who2;`|Shows CPU time, status, login, host, etc.|
|`sp_lock`|Shows locks currently held|`EXEC sp_lock;`|Useful for debugging deadlocks.|
|`sp_helpindex`|Lists indexes for a table|`EXEC sp_helpindex 'products';`|Shows index names, columns, and uniqueness.|
|`sp_configure`|Views or changes server-level settings|`EXEC sp_configure;`|Use with `RECONFIGURE` to apply changes.|
|`sp_spaceused`|Shows how much space a table or DB uses|`EXEC sp_spaceused 'products';`|Returns row count, reserved size, data size, etc.|
|`sp_executesql`|Executes dynamic SQL safely with parameters|`EXEC sp_executesql @sql, N'@x INT', @x=10;`|Safer alternative to `EXEC(@sql)`.|
|`sp_depends`|Lists dependencies (what uses what)|`EXEC sp_depends 'products';`|Deprecated — use `sys.sql_expression_dependencies` now.|
|`sp_MSforeachtable` (undocumented)|Loops over all tables|`EXEC sp_MSforeachtable 'PRINT ''?''';`|Handy for batch operations.|
