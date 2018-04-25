import pandas as pd
import util_functions as uf
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Trip Frequency Count for entire pilot by Operator
    df = pd.read_sql("""select distinct
                        user_freqs.operatorclean,
                        user_freqs.user_trips,
                        count(*) as freq_user_trips
                        from
                        ((select distinct
                        operatorclean,
                        userid,
                        count(*) as user_trips
                        from dockless_trips
                        where operatorclean in ('mobike', 'lime', 'spin')
                        group by 1, 2
                        order by operatorclean, count(*))
                        union
                        /*ofo users*/
                        (select distinct
                        'ofo' as operatorclean,
                        userid,
                        sum(trips) as user_trips
                        from ofo_users
                        group by 1, 2
                        order by operatorclean, sum(trips))
                        union
                        /*jump users*/
                        (select distinct
                        'jump' as operatorclean,
                        userid,
                        sum(trips) as user_trips
                        from jump_users
                        group by 1, 2
                        order by operatorclean, sum(trips))) as user_freqs
                        group by 1, 2
                        order by 1, 2;
                     """, con=conn)

    # Initialize Excel Instance
    writer = pd.ExcelWriter('Dockless_User_Frequency_Analysis.xlsx')

    for operator in df['operatorclean'].drop_duplicates().tolist():
        # Use Jump Data as a test case
        operator_df = df[df['operatorclean'] == operator].copy()

        # Calculate Cumulative Sum and Perc
        operator_df['cumulative_sum'] = operator_df['freq_user_trips'].cumsum()
        operator_df['cumulative_percent'] = operator_df['cumulative_sum']/operator_df['freq_user_trips'].sum()

        # Output to Excel
        operator_df.to_excel(writer, sheet_name=operator, index=False)

    writer.save()
