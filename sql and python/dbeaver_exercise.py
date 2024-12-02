import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert
from flask import Flask, jsonify

# Flask Application
app = Flask(__name__)

# Database Connection (with SQLAlchemy)
DATABASE_URL = "postgresql://consultants:WelcomeItc%402022@18.132.73.146:5432/testdb"
engine = create_engine(DATABASE_URL)

# Creating Table using SQLAlchemy Metadata
metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),  # 'id' column as primary key
    Column('name', String),                   # 'name' column as string type
    Column('age', Integer)                    # 'age' column as integer type
)

# Create the Table in the database (if it doesn't already exist)
metadata.create_all(engine)

# Function to Load Data from CSV File to SQL Database
def load_csv_to_sql(csv_file):
    # Read CSV file using Pandas
    df = pd.read_csv(csv_file)
    # Load CSV data into the 'users' table in SQL
    df.to_sql('users', engine, if_exists='append', index=False)  # Append data without the index column
    print("CSV data successfully loaded into the database!")

# Function to Insert Data into Database
def insert_data_to_db(name, age):
    with engine.connect() as connection:
        connection.execute(insert(users_table).values(name=name, age=age))  # Insert data into the 'users' table
    print(f"Data added: {name}, {age}")

# Flask API: Fetch Data from the Database
@app.route('/get_users', methods=['GET'])
def get_users():
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM users").fetchall()  # Select all rows from the 'users' table
    users = [{"id": row[0], "name": row[1], "age": row[2]} for row in result]  # Format the results as a list of dictionaries
    return jsonify(users)  # Return the data as JSON

# Flask API: Load CSV Data into the Database
@app.route('/load_csv', methods=['POST'])
def load_csv():
    # Here, I've hardcoded the file path. In a real scenario, you could upload the file via an API.
    load_csv_to_sql(r'C:\Users\karab\Desktop\Self-Learning\self-learning-activities\sqlandpython\exercise.py')
    return "CSV data successfully loaded!", 200

# Main Application
if __name__ == '__main__':
    # Example Data Insertion
    insert_data_to_db('John Doe', 30)  # Insert example data
    insert_data_to_db('Jane Smith', 25)  # Insert example data
    
    # Start the Flask API
    app.run(debug=True)
