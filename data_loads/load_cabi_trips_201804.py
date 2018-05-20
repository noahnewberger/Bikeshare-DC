import pandas as pd
import os
import util_functions as uf

# Define function to pull CaBi Trip data from DDOT source


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Convert 2018 01 02 trip data from CSV to dataframe
    combined_df = pd.read_csv(os.path.join("data", '201804-capitalbikeshare-tripdata.csv')).drop(['Start station', 'End station'], axis=1)
    combined_df.columns = ['duration', 'start_date', 'end_date', 'start_station', 'end_station', 'bike_number', 'member_type']
    # Add trip_id continuing from last record in AWS table
    trip_id_df = pd.read_sql("""SELECT trip_id from cabi_trips order by trip_id desc LIMIT 1 """, con=conn)
    last_trip_id = trip_id_df['trip_id'].iloc[0]
    combined_df.reset_index(inplace=True)
    combined_df['trip_id'] = combined_df.index + 1 + last_trip_id
    # Drop unneeded fields
    combined_df.drop(['index'], axis=1, inplace=True)

    # Output dataframe as CSV
    # Define start and end months based on file names
    outname = "CaBi_Trip_Data_201804"
    combined_df.to_csv(os.path.join("data", outname + ".csv"), index=False, sep='|')

    # Load to Database
    uf.aws_load(outname, "cabi_trips", cur)

    # Commit changes to database
    conn.commit()
