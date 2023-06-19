
import psycopg2
from psycopg2.extensions import AsIs
import os

from dotenv import load_dotenv

load_dotenv()
database = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(database=database,
                        user=user, password=password, 
                        host='172.26.0.2', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = "CREATE TABLE ITEMS(\
    product_id time,\
    category_id integer,\
    category_code bigint,\
    brand varchar(8));"

cursor.execute(sql)

sql2 = "COPY ITEMS(product_id,category_id,\
category_code,brand)\
FROM '/00/subject/customer/items.csv'\
DELIMITER ','\
CSV HEADER;"

cursor.execute(sql2)

print("Added items")

conn.commit()
conn.close()
