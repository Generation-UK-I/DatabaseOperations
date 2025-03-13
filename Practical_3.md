# Practical 3
## Insert Records into a Table

Your objective is to create two tables, insert some records into them, then update those records using appropriate SQL commands and syntax. 

Some simple sample SQL statements have been provided below, but you're encouraged to try and use your own scenario and create tables and records to match.

NOTE: If not already doing so, it is recommended that you develop your SQL statements in a separate text editor (not a word processor) and copy/paste them into your SQL session. This makes you statements easier to re-use, and we will be doing so.

### Sample code
Create a customers table:

```sql
CREATE TABLE customers (
	customer_ID INT NOT NULL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	age INT UNSIGNED NOT NULL
);
```
Create a products table:

```sql
CREATE TABLE products (
    product_id INT NOT NULL PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2)
);
```

Populate the customers table:

```sql
INSERT INTO customers (customer_id, first_name, last_name, age)
VALUES
    (5, 'Frankie', 'Foy', 5),
	(6, 'Scout', 'Foy', 2),
	(7, 'John', 'McClane', 53)
	;
```

Populate the products table:

```sql
INSERT INTO products (product_id, product_name, product_price)
VALUES
    (101, 'Ryzen 7 Laptop', 999.99),
    (102, 'iPhone 13', 599.99),
	(103, '27" Monitor', 199.99)
	;
```

Verify records in the customers table:

```sql
SELECT * FROM customers;
```

Verify records in the products table:

```sql
SELECT * FROM products;
```

Update a record in customers:

```sql
UPDATE customers
SET Age = 51
WHERE customer_ID = 7;
```