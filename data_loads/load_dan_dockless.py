import pandas as pd
import util_functions as uf

if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Load raw CSV as Dataframe
    raw_df = pd.read_csv('/home/user/Downloads/gw_capstone_201803011907.csv')
    # Output dataframe as CSV
    outname = "dan_dockless"
    raw_df.to_csv(outname + ".csv", index=False, sep='|')

    # Load to Database
    uf.aws_load(outname, "dan_dockless", cur)

    # Commit changes to database
    conn.commit()
