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
import datetime as dt
if __name__ == '__main__':
    '''
    Distribution of Dockless Trips by Hour
    [[PLOT]]
    '''
    conn = read_only_connect_aws()

    df = pd.read_sql("""SELECT DISTINCT
                        op_trips.*,
                        dow_total_trips,
                        op_trips.dockless_trips/dow_total_trips::float as op_perc
                        FROM
                        /* Get dockless trips by day of week and metro operating status*/
                        (SELECT DISTINCT
                        day_of_week,
                        op_status,
                        COUNT(trips.*) AS dockless_trips
                        from dockless_trips AS trips
                        LEFT JOIN metro_hours AS hours
                        ON extract('DOW' FROM trips.startutc) = hours.day_of_week
                        AND trips.startutc::time BETWEEN hours.start_time AND hours.end_time
                        GROUP BY 1, 2
                        ORDER BY 1, 2) as op_trips
                        /* Get dockless trips by day of week to calculate % of DOW for each metro operating status*/
                        LEFT JOIN
                            (SELECT DISTINCT extract('DOW' FROM startutc) as dow,
                                             count(*) as dow_total_trips
                                             from dockless_trips
                                             group by 1) as dow_trips
                        ON dow_trips.dow = op_trips.day_of_week
                        ORDER BY 1, 2;
                        """, con=conn)
    print(df.head())

    # Open google drive connection
    dr = open_drive()
    df['trips_standardized'] = df['dockless_trips'] / df['dockless_trips'].sum()
    ax = sns.barplot(x='day_of_week', y='trips_standardized', hue='op_status', data=df)
    ax.set_xticklabels(
        ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    all_in_one_save(
        "Dockless Hours of the Week", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1LRJWj6wLBWvyBJbN93jXA2dpgF3BLrN3')
