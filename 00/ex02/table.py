
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
database = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(database=database,
                        user=user, password=password, 
                        host='172.24.0.3', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''
CREATE TABLE DATA_2022_OCT(
    event_time time NOT NULL,\
    event_type varchar(16),\
    product_id integer,\
    price float8,\
    user_id bigint,\
    user_session char(36));'''
  
cursor.execute(sql)
  
sql2 = '''COPY DATA_2022_OCT(event_time,event_type,\
product_id,price,user_id,user_session)
FROM '/00/subject/customer/data_2022_oct.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)

print("Executed all")

conn.commit()
conn.close()
