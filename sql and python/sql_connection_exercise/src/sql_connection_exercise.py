import mysql.connector as con
import pandas as pd

# Create a connection
db_connection = con.connect(
    host="localhost",
    user="root",
    password="355355",
    database="new_schema",
)

# Check the connection
if db_connection.is_connected():
    print("Bağlantı başarılı!")

# Creating a Cursor
cursor = db_connection.cursor()

# INSERT
sql_query = """
    INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary, Email)
    VALUES
        (11, 'Muhammed', 'Elci', 'IT', 2344, 'kara34@hotmail.com'),
        (13, 'Ali', 'Kara', 'Marketing', 232344, 'kar3445534@hotmail.com')
"""

try:
    # Add Data
    cursor.execute(sql_query)

    # Save the updates
    db_connection.commit()

    print("Successfull.")
except Exception as e:
    # Rollback
    db_connection.rollback()
    print(f"Error: {e}")

# Create a Query
try:
    cursor.execute("SELECT FirstName FROM employees")
    data = cursor.fetchall()  # Verileri al

    print("Data:")
    for row in data:
        print(row)

except Exception as e:
    print(f"Query Error: {e}")

# Close the connection
db_connection.close()
cursor.close()
