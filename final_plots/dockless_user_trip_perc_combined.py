import pandas as pd
import sys
import seaborn as sns
sys.path.append("..")
import util_functions as uf
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    conn, cur = uf.local_connect()

    '''Stacked Bar Chart showing % of trips taken by users who took 5 trips or less
    vs greater than 5 trips. One bar for each operator for the entire pilot
    (except Mobike)
    '''
    df = pd.read_sql("""select distinct
                        user_freqs.user_trips,
                        count(*) as freq_user_trips
                        from
                        ((select distinct
                        operatorclean,
                        userid,
                        count(*) as user_trips
                        from dockless_trips
                        where operatorclean in ('lime', 'spin', 'jump')
                              AND userid != '0'
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
                        order by operatorclean, sum(trips))) as user_freqs
                        group by 1
                        order by 1;
                     """, con=conn)
    # Additional data manipulation
    df['le_5'] = np.where(df['user_trips'] <= 5, 0, 1)
    le_5_df = df[['le_5', 'freq_user_trips']].groupby(['le_5'])['freq_user_trips'].sum().to_frame()
    le_5_df['perc_user_trips'] = le_5_df['freq_user_trips'] / le_5_df['freq_user_trips'].sum()
    # Plot
    # Pie chart
    labels = ['<= 5 Trips', '> 5 trips']
    sizes = le_5_df['perc_user_trips'].tolist()
    #colors
    colors = ['#66b3ff','#ffcc99']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    plt.savefig('users_pie.png')
