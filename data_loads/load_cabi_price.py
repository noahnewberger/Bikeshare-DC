import pandas as pd
import util_functions as uf

# This script loads data to the dark_sky_raw AWS table


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Read in Overage Data
    csv_name = "CaBiOverageCosts"
    overage_df = pd.read_csv(csv_name + ".csv")
    # Output final dataframe
    outname = csv_name + "pipe_delimited"
    overage_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "cabi_price", cur)
    # Commit changes to database
    conn.commit()