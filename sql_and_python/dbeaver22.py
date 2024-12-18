from flask import Flask,request,jsonify
from sqlalchemy import create_engine

app=Flask(__name__)

filePath = "D:\\SampleData\\customer1.csv"
myTableName = "customer1"
username = "consultants"
password = "WelcomeItc%402022"
host = "18.132.73.146"
databaseName = "testdb"
port = 5432

def connect_to_sql():
    try:

        engine=create_engine('postgresql://{username}:{password}@{host}:{port}/{databaseName}'.format(
            username=username,
            password=password,
            host=host,
            port=port,
            databaseName=databaseName
        ))

        return engine
    
    except Exception as e:
        print('Error is : {e}'.format(e=e))

def close(engine):
    if engine:
        engine.dispose()
        print('Connection closed')







