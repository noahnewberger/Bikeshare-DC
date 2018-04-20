import pandas as pd
import os
import util_functions as uf

# TODO: Define function to pull CaBi Trip data from DDOT source


def trips_to_df(cabi_trip_dir):
    # Loop through CSVs of Trip Data
    trip_df_list = []
    csv_list = [f for f in os.listdir(cabi_trip_dir) if f.endswith('.txt')]
    for csv in csv_list:
        csv_name = csv.replace('.txt', '')
        print("{} has started processing".format(csv_name))
        # Load original CSV as dataframe
        trip_df = pd.read_csv(os.path.join(cabi_trip_dir, csv_name + '.txt'), delimiter="|")
        keep_cols = ["Startdate", "Enddate", "StartStationNumber", "EndStationNumber", "Bikenumber", "MemberType"]
        trip_df = trip_df[keep_cols]
    combined_df = pd.concat(trip_df_list, axis=0)
    return combined_df


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Loop through all CSVs in cabi trip data folder
    cabi_trip_dir = r'./data/Cabi_Trips_MemberType'

    # Convert trip data from CSV to dataframe
    combined_df = trips_to_df(cabi_trip_dir)

    # Add trip_id
    combined_df['trip_id'] = combined_df.index + 1

    # Output dataframe as CSV
    outname = "Cabi_Trips_MemberType"
    combined_df.to_csv(os.path.join("data", outname + ".csv"), index=False, sep='|')

    import sys
    sys.exit()

    # Load to Database
    uf.aws_load(outname, "cabi_trips_membertype", cur)

    # Commit changes to database
    conn.commit()
