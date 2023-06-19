
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

for filename in os.listdir("../00/subject/customer/"):
    nameSplit = filename.split(".", 1)[0]

    sql = "CREATE TABLE %s(\
        event_time time NOT NULL,\
        event_type varchar(16),\
        product_id integer,\
        price float8,\
        user_id bigint,\
        user_session char(36));"
    
    cursor.execute(sql, (AsIs(nameSplit.upper()),))
    
    sql2 = "COPY %s(event_time,event_type,\
    product_id,price,user_id,user_session)\
    FROM '/00/subject/customer/%s.csv'\
    DELIMITER ','\
    CSV HEADER;"
    
    cursor.execute(sql2, (AsIs(nameSplit.upper()), AsIs(nameSplit),))

    print("Added " + filename)

conn.commit()
conn.close()
