import requests
import pandas as pd
import numpy as np
import util_functions as uf


def pull_station_info():
    # Load CaBI region information from API
    station_url = "https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json"
    stations = requests.get(station_url).json()
    station_df = pd.DataFrame(stations['data']['stations'])
    return station_df


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Pull CaBi System Regions
    station_df = pull_station_info()
    # Default any missing region ids to DC (only example as of 2/21 is new station at Anacostia Park)
    station_df['region_id'] = np.where(station_df['region_id'].isnull(), 42, station_df['region_id'])
    station_df['region_id'] = station_df['region_id'].astype(int)
    # Output dataframe as CSV
    outname = "CaBi_Stations_Temp"
    station_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "cabi_stations_temp", cur)
    # Commit changes to database
    conn.commit()
