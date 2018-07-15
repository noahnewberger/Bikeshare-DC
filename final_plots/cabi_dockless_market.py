import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import re
import datetime
import os
import shutil
sys.path.append("..")
import util_functions as uf


# Lists for graphing metrics
distance = [
    'cabi_trip_dist_avg_wdc_to_wdc', 'dless_tripdist_avg_jump',
    'dless_tripdist_avg_lime', 'dless_tripdist_avg_mobike',
    'dless_tripdist_avg_ofo', 'dless_tripdist_avg_spin']

trips_agg = [
    'cabi_trips_wdc_to_wdc', 'cabi_trips_wdc_to_wdc_member',
    'cabi_trips_wdc_to_wdc_casual', 'dless_trips_all']

trips_gran = [
    'cabi_trips_wdc_to_wdc', 'dless_trips_jump', 'dless_trips_lime',
    'dless_trips_mobike', 'dless_trips_ofo', 'dless_trips_spin']

user_all = [
    'cabi_active_members_total', 'dless_users_total',
    'dless_users_jump', 'dless_users_lime', 'dless_users_mobike',
    'dless_users_ofo', 'dless_users_spin']

month_lst = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov',
    12: 'Dec'}


def month_prep(mon):
    # convert float month digit to integer to string month name
    mon = mon.astype(int)
    mon = mon.map(month_lst)
    return mon


if __name__ == '__main__':
    # Loading the final database using a custom class to connect with AWS
    conn, cur = uf.local_connect()
    df = pd.read_sql("""select * from final_db;""", con=conn)
    # Only looking at days with at least one dockless trip
    df = df[df['dless_trips_all'] != 0]
    # Month Converter
    df['month'] = month_prep(df['month'])
    df['date'] = pd.to_datetime(df['date'])
    # Pct Cabi versus Dockless. Casual and total dc to dc trips
    pct_df = df.groupby(['month'])[
        'dless_trips_all',
        'cabi_trips_wdc_to_wdc'].sum().reset_index()
    pct_df['Dockless'] = (
        pct_df['dless_trips_all']/(
            pct_df['dless_trips_all']+pct_df['cabi_trips_wdc_to_wdc'])*100)
    pct_df['Capital Bikeshare'] = (
        pct_df['cabi_trips_wdc_to_wdc']/(
            pct_df['dless_trips_all'] + pct_df['cabi_trips_wdc_to_wdc'])*100)
    # Custom sorting on months
    pct_df['month'] = pd.Categorical(
        pct_df['month'], [
            'Sep', 'Oct', 'Nov', 'Dec',
            'Jan', 'Feb', 'Mar', 'Apr'])
    pct_df.sort_values('month', inplace=True)
    pct_df = pct_df.reset_index()
    pct_df['index'] = pct_df.index.values

    print(pct_df)
    # Creating subplots
    f, axes = plt.subplots(1, 1, figsize=(10, 10))
    p1 = plt.bar(pct_df['month'], pct_df['Capital Bikeshare'], color=['#66b3ff'])
    p2 = plt.bar(pct_df['month'], pct_df['Dockless'], bottom=pct_df['Capital Bikeshare'], color=['#ffcc99'])
    plt.legend((p1[0], p2[0]), ('Capital Bikeshare', 'Dockless'), loc='lower center',
               bbox_to_anchor=(0.5, -0.1), ncol=2)
    # Annotating the graph
    for pat in axes.patches:
        h1 = pat.get_height()
        axes.annotate(str(int(np.around(pat.get_height(), 0)))+'%', (
            pat.get_x() + 0.25, pat.get_y() + pat.get_height()/2),
            fontsize=10)
    plt.savefig('cabi_dless_market.png')
    sys.exit()


