
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
                        host='172.30.0.3', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql = "CREATE TABLE CUSTOMERS(\
    id SERIAL PRIMARY KEY\
    event_time time NOT NULL,\
    event_type varchar(16),\
    product_id integer,\
    price float8,\
    user_id bigint,\
    user_session char(36));"

cursor.execute(sql)

for filename in os.listdir("../../00/00/subject/customer/"):
    print("Adding " + filename + " to customers table")

    sql2 = "COPY CUSTOMERS(event_time,event_type,\
    product_id,price,user_id,user_session)\
    FROM '/00/subject/customer/%s'\
    DELIMITER ','\
    CSV HEADER;"
    
    cursor.execute(sql2, (AsIs(filename),))

    print("Added " + filename + " to customers table\n")

conn.commit()
conn.close()
