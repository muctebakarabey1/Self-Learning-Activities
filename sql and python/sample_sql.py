from sqlalchemy import MetaData, Table,Column,Integer, String,create_engine,Insert,values
from pandas import pd
from flask import Flask, jsonify

DATABASE_URL = "postgresql://consultants:WelcomeItc%402022@18.132.73.146:5432/testdb"

engine=create_engine(DATABASE_URL)

metadata=MetaData()


users_table=Table('users',metadata,
        
        Column('id',Integer,primary_key=True),
        Column('name',String),
        Column('email',String)
      )

metadata.create_all(engine)

def load_csv_to_sql(csv):
    df=pd.read_csv(csv)

    df.to_sql('users_table',engine,if_exists='append',index=False)
    print("CSV data successfully loaded into the database!")


def insert_data_to_db(name,email):
    with engine.connect() as connection:
        connection.execute(Insert(users_table),values(name=name,email=email))
        print(f"Data added: name:{name} email:{email}")


@app.route('/get_user',methods=['GET'])

def get_user():
    with engine.connect









