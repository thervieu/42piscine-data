
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


sql = "DELETE FROM CUSTOMERS a\
    USING CUSTOMERS b\
    WHERE a.id < b.id\
    AND a.event_time = b.event_time\
    AND a.event_type = b.event_type\
    AND a.product_id = b.product_id\
    AND a.user_id = b.user_id\
    AND a.user_session = b.user_session;"

cursor.execute(sql)

conn.commit()
conn.close()
