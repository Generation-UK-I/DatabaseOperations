#first type "python3 -m pip install mysql-connector-python" into terminal
#NOT python3 -m pip install mysql-connector

import mysql.connector

def retrieve_and_display_products():
    # Database connection details
    config = {
        'user': 'admin',  # Replace with your database username
        'password': 'admin',  # Replace with your database password
        'host': '192.168.1.138',  # Replace with your database host
        'database': 'my_shop',  # Replace with your database name
    }

    try:
        # Connect to the database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # SQL query to retrieve products
        query = "SELECT * FROM employees"
        cursor.execute(query)

        # Fetch all rows from the executed query (tuples)
        employees = cursor.fetchall()

        # Display the products
        if employees:
            user_login = input("please enter your username:")
            for x in employees:
                if x[1] == user_login:
                    password = input("please enter your password:")
                    if password == x[2]:
                        print("Login successful...")
                    else:
                        print("password incorrect")
            else:
                print("Please enter valid credentials.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Call the function
retrieve_and_display_products()