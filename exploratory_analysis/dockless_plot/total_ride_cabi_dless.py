import sys
sys.path.append("..")

import numpy as np
from read_aws import *
from google_drive_push import *
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint
import calendar
import re
from dockless_exploration_graphs import *

if __name__ == '__main__':
    conn = read_only_connect_aws()
    plt.style.use('fivethirtyeight')
    '''Stacked Bar Chart showing % of trips taken by users who took 5 trips or less
    vs greater than 5 trips. One bar for each operator for the entire pilot
    (except Mobike)
    '''

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
    dr = open_drive()

    for i in range(1, 6):
        df['le_5'] = np.where(df['user_trips'] <= i, 0, 1)
        le_5_df = df.groupby(
            ['operatorclean', 'le_5'])['freq_user_trips'].sum()
        le_5_df = le_5_df.groupby(level=0).apply(
            lambda x: 100 * x / float(x.sum())).reset_index()

        width = 0.35

        p1 = plt.bar(
            le_5_df['operatorclean'][le_5_df['le_5'] == 0],
            le_5_df['freq_user_trips'][le_5_df['le_5'] == 0], width)
        p2 = plt.bar(
            le_5_df['operatorclean'][le_5_df['le_5'] == 1],
            le_5_df['freq_user_trips'][le_5_df['le_5'] == 1], width,
            bottom=le_5_df['freq_user_trips'][le_5_df['le_5'] == 0])

        plt.legend((p1[0], p2[0]), (
            '<= {0} Trips'.format(i), '> {0} Trips'.format(i)))
        all_in_one_save(
            "dless usage by {0} trips".format(i),
            "C:/Users/Noah/Bikeshare-DC_Old/For Upload",
            dr, '1LRJWj6wLBWvyBJbN93jXA2dpgF3BLrN3')
