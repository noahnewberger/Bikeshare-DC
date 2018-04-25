import pandas as pd
import util_functions as uf
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Trip Frequency Count for entire pilot by Operator
    df = pd.read_sql("""select distinct
                        operatorclean,
                        userid,
                        count(*) as user_trips
                        from dockless_trips
                        where operatorclean in ('mobike')
                        group by 1, 2
                        order by operatorclean, count(*);
                     """, con=conn)
    df.to_csv("mobike.csv", index=False)
    print(df.head())
