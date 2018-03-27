import psycopg2
import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
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
cabi_trips = pd.read_sql("""SELECT duration/60000 as duration_mins, EXTRACT(YEAR FROM start_date) AS year, member_type from cabi_trips LIMIT 10""", con=conn)

#Calculate median and IQR
duration_med = np.percentile(cabi_trips['duration_mins'], 50)
q75, q25 = np.percentile(cabi_trips['duration_mins'], [75 ,25])
iqr = q75 - q25

#Remove values (outliers) that are 3 times IQR away from median
cabi_trips = cabi_trips[cabi_trips['duration_mins'] < duration_med + (3 * iqr)]

#Set plot style
style.use('fivethirtyeight')

#create violin plot
ax = sns.violinplot(x = 'year', y = 'duration_mins', hue = 'member_type', data = cabi_trips)
plt.show()
