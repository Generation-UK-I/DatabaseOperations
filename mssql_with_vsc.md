# Steps to Connect VSC to SQL Server

1. **Install the SQL Server Extension in VSC**

- Open VSC.
- Go to the Extensions view (Ctrl+Shift+X).
- Search for `SQL Server (mssql)` by Microsoft.
- Click Install.

2. Configure the Connection

- After installing, press Ctrl+Shift+P to open the Command Palette.
- Type and select "MS SQL: Connect".
- Fill in the connection details:
  - Server name (e.g., localhost, .\SQLEXPRESS, or IP address)
  - Database name (optional)
  - Authentication type (SQL Login or Windows)
  - Username/Password (if using SQL Login)

3. Write and Run SQL Queries

- Create a new file with the .sql extension.
- Write your SQL queries.
- Right-click and choose "Run Query" or use the command palette.

4. View Results

- Query results will appear in a panel below your code.
- You can export results or copy them as needed.
