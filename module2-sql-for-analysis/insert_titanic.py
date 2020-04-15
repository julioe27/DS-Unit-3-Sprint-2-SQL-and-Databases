import os
import pandas
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
#
# READ CSV
#​
# if your CSV file is in the "data" dir:
CSV_FILEPATH = os.path.join(os.path.dirname(__file__),"titanic.csv")
df = pandas.read_csv(CSV_FILEPATH)
df.index += 1
print(df.head())
#
# CONNECT TO PG DATABASE
#
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
#
# CREATE TABLE
#
table_creation_query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
cursor.execute(table_creation_query)
#
# INSERT DATA IN THE TABLE
#

list_of_tuples = list(df.to_records(index=True))
# possibly sometimes would need to do further transformations, perhaps using a list comprehension
insertion_query = "INSERT INTO passengers (id, survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples)

# SAVE THE RESULTS!
connection.commit()
# CLEAN UP!
cursor.close()
connection.close()