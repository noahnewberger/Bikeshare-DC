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
    def plot_reg_lines(df_s, axis):
        df = df_s
        df['index'] = df.reset_index().index.values
        sns.regplot(
            x='index', y='dless_total_perc', data=df, ax=axis,
            label='Dockless', color='b')
        sns.regplot(
            x='index', y='cabi_total_perc', data=df, ax=axis,
            label='Cabi Total', color='r')
        sns.regplot(
            x='index', y='cabi_casual_perc', data=df, ax=axis,
            label='Cabi Casual', color='g')
        axis.set_xlim(0, len(df))
        xticks = axis.get_xticks()
        xticks = [df['date'].min() + dt.timedelta(days=d) for d in xticks]
        axis.set_xticklabels(xticks)
        axis.xaxis.label.set_visible(False)
        axis.yaxis.label.set_visible(False)

    plt.style.use('fivethirtyeight')
    conn = read_only_connect_aws()
    main = pd.read_sql(
        """select distinct
        date,
        /*Get Daily Percentage by taking daily totals and dividing by pilot totals*/
        (cabi_trips_wdc_to_wdc/cabi_trips_wdc_to_wdc_pilot)*100 as cabi_total_perc,
        (cabi_trips_wdc_to_wdc_casual/cabi_trips_wdc_to_wdc_casual_pilot)*100 as cabi_casual_perc,
        (dless_trips_all/dless_trips_all_pilot)*100 as dless_total_perc
        from final_db as db
        left join
        /*Aggregate Trips for the entire Pilot for CaBi and Dockless Totals*/
        (select
        sum(cabi_trips_wdc_to_wdc) as cabi_trips_wdc_to_wdc_pilot,
        sum(cabi_trips_wdc_to_wdc_casual) as cabi_trips_wdc_to_wdc_casual_pilot,
        sum(dless_trips_all) as dless_trips_all_pilot
        from final_db
        where dless_trips_all > 0) as tot
        on db.date = db.date
        where dless_trips_all > 0;
             """, con=conn)
    print(main.head())

    dr = open_drive()
    f, axes = plt.subplots(1, 2, sharey='row', figsize=(20, 10))

    axes[0].set_title(
        "First Four Trial Months (September 10, 2017 - December 31, 2017)")
    axes[1].set_title(
        "Second Four Trial Months (January 1, 2018 - April 30, 2018)")
    plot_reg_lines(
        main[main['date'] <= dt.date(year=2017, month=12, day=31)], axes[0])
    plot_reg_lines(
        main[main['date'] > dt.date(year=2017, month=12, day=31)], axes[1])
    axes[0].yaxis.label.set_visible(True)
    axes[0].set_ylabel("Daily Percentage of Total Trips")
    handles, labels = axes[0].get_legend_handles_labels()
    f.legend(handles, labels, loc='best')
    all_in_one_save(
        "Dockless Pilot", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1LRJWj6wLBWvyBJbN93jXA2dpgF3BLrN3')
