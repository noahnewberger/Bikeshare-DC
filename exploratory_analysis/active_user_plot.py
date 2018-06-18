import sys
import numpy as np
from read_aws import *
from google_drive_push import *
import seaborn as sns
from seaborn import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from pprint import pprint
import calendar
import re
import datetime
if __name__ == '__main__':
    conn = read_only_connect_aws()

    df = pd.read_sql("""select distinct
                        date,
                        /* Active Users for Individual Dockless Operators*/
                        dless_users_jump,
                        dless_users_lime,
                        dless_users_mobike,
                        dless_users_ofo,
                        dless_users_spin,
                        /* Total Active Users for Dockless Operators*/
                        (dless_users_jump +
                         dless_users_lime +
                         dless_users_mobike +
                         dless_users_ofo +
                         dless_users_spin) as dless_users_total,
                        /* Total Active Users */
                        (cabi_active_members_day_key +
                        cabi_active_members_monthly +
                        cabi_active_members_annual) as cabi_active_members_total
                        from final_db
                        where dless_trips_all > 0
                        """, con=conn)
    print(df.tail())

    dr = open_drive()
    # Utilization by Vendor

    df = pd.melt(
        df, id_vars=['date'], var_name='Category', value_name='users'
        )
    df.replace(0,np.nan, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['operator'] = df['Category'].str.split('_').str.get(2)
    df['operator'].replace('members', 'cabi', inplace=True)
    df['operator'].replace('total', 'dockless', inplace=True)
    df['count'] = df.groupby(['operator']).cumcount()+1
    f, ax = plt.subplots(figsize=(12, 8))
    axis = sns.tsplot(
        time='count', value='users', unit='operator', condition='operator',
        data=df, ax=ax)
    axis.set_xlim(0, len(df[df['operator'] == 'cabi']))
    axis.xaxis.set_major_locator(ticker.MultipleLocator(10))
    xticks = axis.get_xticks()
    xticks = [df['date'].min() + datetime.timedelta(days=int(d)) for d in xticks]
    xticks = [x.strftime("%m/%d/%y") for x in xticks]
    axis.set_xticklabels(xticks, rotation=45)
    axis.set_xlabel('Date')
    axis.set_ylabel('User Count')

    all_in_one_save(
        "Active Users Final", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1LRJWj6wLBWvyBJbN93jXA2dpgF3BLrN3')
