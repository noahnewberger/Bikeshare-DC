import psycopg2
import pandas as pd
import os
import getpass

host = "capstone-bikeshare.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
port = 5432
database = "bikeshare"
user = input("Enter your user name: ")
password = getpass.getpass("Enter your password: ")


# Connect to aws postgres DB
conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
cur = conn.cursor()

# Format Data as necessary in dataframe and then upload formatted version
cabi_out_dir = '../production/'
csv_name = "CaBi_Tracker_Outage_History_From_2011-05-01_To_2018-02-28"
print("{} has started processing".format(csv_name))

# Load original CSV as dataframe
out_hist_df = pd.read_csv(os.path.join(cabi_out_dir, csv_name + '.csv')).drop(['Station Name'], axis=1)
out_hist_df.columns = ['terminal_number', 'status', 'start_time', 'end_time', 'duration']

# Export as CSV
todb_csv = csv_name + "_formatted"
todb_path = os.path.join(cabi_out_dir, todb_csv + '.csv')
out_hist_df.to_csv(todb_path, index=False)

# Load to Database
with open(todb_path, 'r') as f:
    # Skip the header row.
    next(f)
    cur.copy_from(f, 'cabi_out_hist', sep=',')
print("{} has been loaded to the cabi_out_hist database".format(csv_name))

# Add big serial as Primary Key
cur.execute("ALTER TABLE cabi_out_hist ADD COLUMN outage_id BIGSERIAL PRIMARY KEY")

# Commit changes to database
conn.commit()
