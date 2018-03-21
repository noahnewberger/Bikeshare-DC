import psycopg2
import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

host = "capstone-bikeshare.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
port = 5432
database = "bikeshare"

user = os.environ.get("AWS_READONLY_USER")
password = os.environ.get("AWS_READONLY_PASS")


# Connect to aws postgres DB
conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
cur = conn.cursor()

# Query cabi trips
df = pd.read_sql("""SELECT * from cabi_trips LIMIT 10""", con=conn)

print(df)
print(df.dtypes)
