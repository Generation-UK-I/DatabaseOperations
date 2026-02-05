# SQL functions and operators:

## **AGGREGATE FUNCTIONS**
Perform calculations on multiple rows and return a single value:
```sql
-- Common aggregate functions
SUM()     -- Sum of values
AVG()     -- Average of values
MIN()     -- Minimum value
MAX()     -- Maximum value
COUNT()   -- Count of rows
STDDEV()  -- Standard deviation
VARIANCE()-- Variance

-- Examples
SELECT SUM(salary) FROM employees;
SELECT AVG(age) FROM users;
SELECT MIN(price), MAX(price) FROM products;
```

## **CONVERSION FUNCTIONS**
Convert data from one type to another:
```sql
-- Common across databases
CAST(expression AS type)           -- Standard SQL
CONVERT(type, expression)          -- SQL Server, MySQL

-- Database-specific examples
-- MySQL
CONVERT('2023-01-01', DATE)
CAST('123' AS UNSIGNED)

-- SQL Server
CONVERT(VARCHAR, GETDATE(), 101)
CAST(price AS DECIMAL(10,2))

-- Oracle
TO_CHAR(salary, '$999,999')
TO_DATE('2023-01-01', 'YYYY-MM-DD')
TO_NUMBER('123.45')
```

## **DATE FUNCTIONS**
Work with date and time values:
```sql
-- Common functions
CURRENT_DATE / GETDATE() / NOW()  -- Current date
DATEDIFF(date1, date2)            -- Difference between dates
DATE_ADD(date, INTERVAL)          -- Add to date
DATE_FORMAT(date, format)         -- Format date
EXTRACT(part FROM date)           -- Extract part (YEAR, MONTH, etc.)

-- Examples
SELECT DATE_ADD('2023-01-01', INTERVAL 7 DAY);  -- MySQL
SELECT DATEDIFF(day, '2023-01-01', '2023-01-08'); -- SQL Server
SELECT EXTRACT(YEAR FROM birth_date) FROM employees;
```

## **STRING FUNCTIONS**
Manipulate text data:
```sql
-- Common string functions
CONCAT(str1, str2, ...)       -- Combine strings
UPPER() / LOWER()              -- Change case
TRIM() / LTRIM() / RTRIM()     -- Remove spaces
LENGTH() / LEN()               -- String length
SUBSTRING(str, start, length) -- Extract substring
REPLACE(str, old, new)         -- Replace text

-- Examples
SELECT CONCAT(first_name, ' ', last_name) AS full_name;
SELECT UPPER(product_name) FROM products;
SELECT SUBSTRING(email, 1, 5) FROM users;
```

## **MATHEMATICAL FUNCTIONS**
Perform mathematical operations:
```sql
-- Common math functions
ABS(x)        -- Absolute value
ROUND(x, d)   -- Round to decimal places
CEILING()     -- Round up
FLOOR()       -- Round down
POWER(x, y)   -- x raised to power y
SQRT(x)       -- Square root
MOD(x, y)     -- Modulo/remainder

-- Examples
SELECT ROUND(price * 1.08, 2) AS price_with_tax;
SELECT ABS(temperature_change) FROM readings;
SELECT FLOOR(average_score) FROM students;
```

## **CONTROL FLOW FUNCTIONS**
Conditional logic in SQL:
```sql
-- Common control flow
CASE WHEN condition THEN result ELSE other END
IF(condition, true_value, false_value)    -- MySQL
IIF(condition, true_value, false_value)   -- SQL Server
COALESCE(value1, value2, ...)             -- Return first non-null
NULLIF(expr1, expr2)                      -- Return NULL if equal

-- Examples
SELECT 
    CASE 
        WHEN grade >= 90 THEN 'A'
        WHEN grade >= 80 THEN 'B'
        ELSE 'C'
    END AS letter_grade
FROM scores;

SELECT COALESCE(middle_name, 'N/A') FROM persons;
```

## **DISTINCT**
Removes duplicate rows from result set:
```sql
-- Get unique values
SELECT DISTINCT department FROM employees;

-- Count unique values
SELECT COUNT(DISTINCT country) FROM customers;

-- Multiple columns
SELECT DISTINCT city, state FROM addresses;
```

## **COUNT**
Counts rows in a result set:
```sql
-- Basic count
SELECT COUNT(*) FROM products;           -- All rows

-- Count non-null values
SELECT COUNT(email) FROM users;          -- Only non-null emails

-- Count distinct values
SELECT COUNT(DISTINCT category) FROM products;

-- Count with conditions
SELECT COUNT(*) FROM orders WHERE status = 'shipped';

-- Count with GROUP BY
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department;
```

## **KEY DIFFERENCES**

1. **COUNT(*) vs COUNT(column):**
   ```sql
   COUNT(*)          -- Counts all rows including NULLs
   COUNT(column)     -- Counts non-NULL values in specific column
   ```

2. **DISTINCT placement matters:**
   ```sql
   SELECT COUNT(DISTINCT department)  -- Count unique departments
   SELECT DISTINCT COUNT(department)  -- Usually doesn't make sense
   ```

3. **Aggregate functions ignore NULL values** (except COUNT(*))