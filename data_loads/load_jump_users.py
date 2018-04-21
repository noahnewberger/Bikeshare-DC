import pandas as pd
import os
import util_functions as uf
from datetime import datetime


def convert_month_toDT(x):
    # Convert text month to datetime
    if x in [9, 10, 11, 12]:
        date = datetime(year=2017, month=x, day=1)
    else:
        date = datetime(year=2018, month=x, day=1)
    return date


def create_jump_users(cur):
    # This script creates the CaBi Stations Geo Temp AWS table
    cur.execute("""
    DROP TABLE IF EXISTS jump_users;
    CREATE TABLE jump_users(
        userid varchar(30),
        trips integer,
        usage_month date
        );
            """)


if __name__ == "__main__":

    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Load Ofo user from report provided by DDOT
    user_report_loc = os.path.join("data", "User ids.xlsx")
    jump_df = pd.read_excel(user_report_loc, sheet_name="JUMP User Trips", index_col='User ID')
    # Drop Grand total row and stack columns
    jump_df.drop(['Grand Total'], axis=1, inplace=True)
    jump_df_stack = jump_df.stack()
    jump_df_stack = jump_df_stack.reset_index()

    # Define Month in Datetime
    jump_df_stack['usage_month'] = jump_df_stack['level_1'].apply(convert_month_toDT)
    jump_df_stack.drop(['level_1'], axis=1, inplace=True)
    jump_df_stack.columns = ['user_id', 'trips', 'usage_month']
    jump_df_stack.sort_values(['user_id', 'usage_month'], inplace=True)

    # Convert Trips to Integer;
    jump_df_stack['trips'] = jump_df_stack['trips'].astype(int)

    # Output dataframe as CSV
    outname = "jump_users"
    jump_df_stack.to_csv(os.path.join("data", outname + ".csv"), index=False, sep='|')

    # Create Table in AWS
    create_jump_users(cur)

    # Load to Database
    uf.aws_load(outname, "jump_users", cur)

    # Commit changes to database
    conn.commit()
