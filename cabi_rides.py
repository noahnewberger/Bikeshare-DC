import psycopg2
import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import datetime as dt
import matplotlib.style as style
import matplotlib.pyplot as plt
import seaborn as sns

env_path = Path() / '.env'
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
cabi_trips = pd.read_sql("""SELECT duration/60000 as duration_mins, start_date, EXTRACT(MONTH FROM start_date) AS month, member_type from cabi_trips WHERE EXTRACT(YEAR FROM start_date) = 2016 LIMIT 100000""", con=conn)

cabi_trips = cabi_trips.loc[cabi_trips['duration_mins'] < 120]
#Set plot style
style.use('fivethirtyeight')

plt.hist(cabi_trips['duration_mins'], bins = 50)
plt.show()

#create violin plot
#ax = sns.violinplot(x = 'month', y = 'duration_mins', hue = 'member_type', data = cabi_trips)
#plt.show()
