import util_functions as uf
import pandas as pd

if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Load CSV FROM IPMUS Download as Dataframe
    csv_name = 'usa_00007'
    acs_df = pd.read_csv(csv_name + ".csv")
    # Set Primary Key
    acs_df.reset_index(inplace=True)
    # Fill all na with zeros
    acs_df.fillna(0, inplace=True)
    # Output dataframe as CSV
    outname = csv_name + "_pipe_delimited"
    acs_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "acs", cur)
    # Commit changes to database
    conn.commit()
