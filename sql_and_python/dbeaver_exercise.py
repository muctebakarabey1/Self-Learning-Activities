import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy import create_engine
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
import pandas as pd


filePath = "D:\\SampleData\\customer1.csv"
myTableName = "customer1"
username = "consultants"
password = "WelcomeItc%402022"
host = "18.132.73.146"
databaseName = "testdb"
port = 5432

app = Flask(__name__)

# Connect to PostgreSQL function (to be tested)
def connect_to_postgres():
    try:
        # Create an engine to connect to PostgreSQL
        engine = create_engine('postgresql://{username}:{password}@{host}:{port}/{databaseName}'.format(
            username=username,
            password=password,
            host=host,
            port=port,
            databaseName=databaseName
        ))
        print("Connection to PostgreSQL established successfully.")
        return engine
    except Exception as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None


# Unit Test for connect_to_postgres function
class TestDatabaseConnection(unittest.TestCase):
    
    @patch('sqlalchemy.create_engine')  # Mock create_engine
    def test_connection_success(self, mock_create_engine):
        # Mock the successful return value of create_engine (simulating a successful connection)
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        
        # Call the function to test
        engine = connect_to_postgres()
        
        # Assert that the engine was created successfully
        mock_create_engine.assert_called_once_with(
            'postgresql://{username}:{password}@{host}:{port}/{databaseName}'.format(
                username=username,
                password=password,
                host=host,
                port=port,
                databaseName=databaseName
            )
        )
        self.assertEqual(engine, mock_engine)
    
    @patch('sqlalchemy.create_engine')  # Mock create_engine
    def test_connection_failure(self, mock_create_engine):
        # Mock the case where create_engine raises an exception (simulating a failed connection)
        mock_create_engine.side_effect = Exception("Connection failed")
        
        # Call the function to test
        engine = connect_to_postgres()
        
        # Assert that the result is None since the connection failed
        self.assertIsNone(engine)

# Route to fetch data from PostgreSQL database
@app.route('/get_data', methods=['GET'])
def get_data():
    # Connect to the database
    engine = connect_to_postgres()
    if engine is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Example: Querying a table (replace 'your_table' with your actual table name)
        result = session.execute('SELECT * FROM "customer1" LIMIT 10;')
        data = result.fetchall()

        # Convert the query result into a list of dictionaries
        result_list = [dict(zip(result.keys(), row)) for row in data]

        # Return the result as JSON
        return jsonify(result_list)

    except Exception as error:
        return jsonify({"error": "Error querying the database: error"}), 500
    finally:
        session.close()

def main():

    engine = connect_to_postgres()
    if engine is not None:
        df = pd.read_csv(filePath)
        if df is not None:
            table_name = myTableName
            df.to_sql(table_name, engine, if_exists='replace', index=False)
        engine.dispose()

if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=5315, debug=True)


    

