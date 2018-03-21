import psycopg2
import pandas as pd
import os

# Connect to local postgres DB
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()


# Loop through all CSVs in cabi trip data folder
cabi_trip_dir = '../cabi_trip_data'

for csv in sorted(os.listdir(cabi_trip_dir)):
    csv_name = csv.replace('.csv', '')
    print("{} has started processing".format(csv_name))
    # Load original CSV as dataframe
    trip_df = pd.read_csv(os.path.join(cabi_trip_dir, csv_name + '.csv')).drop(['Start station', 'End station'], axis=1)
    trip_df.columns = ['duration', 'start_date', 'end_date', 'start_station', 'end_station', 'bike_number', 'member_type']

    # Export as CSV
    todb_csv = csv_name + "_formatted"
    todb_path = os.path.join(cabi_trip_dir, todb_csv + '.csv')
    trip_df.to_csv(todb_path, index=False)

    # Load to Database
    with open(todb_path, 'r') as f:
        # Skip the header row.
        next(f)
        cur.copy_from(f, 'cabi_trips', sep=',')
    print("{} has been loaded to the cabi_trips database".format(csv_name))

# Add big serial as Primary Key
cur.execute("ALTER TABLE cabi_trips ADD COLUMN trip_id BIGSERIAL PRIMARY KEY")

# Commit changes to database
conn.commit()
