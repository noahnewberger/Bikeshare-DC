import pandas as pd
import util_functions as uf
import numpy as np

# This script loads data to the dockless_price AWS table


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Read in Overage Data
    csv_name = "feburaryaddedutc"
    trips_df = pd.read_csv(csv_name + ".csv", index_col=[0], dtype=str)
    # List of all duplicate records by TripID
    '''try:
        dupes_by_trip = pd.concat(g for _, g in trips_df.groupby(["TripID"]) if len(g) > 1)
        print("{} duplicate records by TripID".format(len(dupes_by_trip)))
    except:
        print("No duplicate records by TripID")
    try:
        dupes_by_operator_trip = pd.concat(g for _, g in trips_df.groupby(["Operator", "TripID"]) if len(g) > 1)
        print("{} duplicate records by TripID".format(len(dupes_by_trip)))
    except:
        print("No duplicate records by Operator and TripID")'''
    print(len(trips_df['TripID']))
    print(len(trips_df['TripID'].drop_duplicates()))
    # Drop duplicate records by Operator and TripID
    trips_df = trips_df.drop_duplicates(["Operator", "TripID"])
    print(len(trips_df['TripID']))
    # Fill missing with 0
    trips_df.fillna(0, inplace=True)
    # Create a new trip_id that includes the first letter of the operator name
    trips_df['UniqueTripID'] = trips_df['Operator'].str[0] + trips_df['TripID']
    # Drop records without an Operator
    trips_df = trips_df[trips_df['Operator'] != 0]
    # Create clean version of operator
    trips_df['OperatorClean'] = trips_df['Operator'].map(lambda x: x.split(" ")[0].lower().replace('limebike', 'lime'))
    # Set enddate equal to startdate if missing
    trips_df['EndDate'] = np.where(trips_df['EndDate'] == 0, trips_df['StartDate'], trips_df['EndDate'])
    trips_df['endposct'] = np.where(trips_df['endposct'] == 0, trips_df['posct'], trips_df['endposct'])
    trips_df['endutc'] = np.where(trips_df['endutc'] == 0, trips_df['startutc'], trips_df['endutc'])
    # Output final dataframe
    outname = csv_name + "pipe_delimited"
    trips_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "dockless_trips", cur)
    # Commit changes to database
    conn.commit()
