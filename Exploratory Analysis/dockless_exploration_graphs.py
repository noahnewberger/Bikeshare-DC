import sys
import numpy as np
from read_aws import *
from google_drive_push import *
import seaborn as sns
from seaborn import *
import matplotlib.pyplot as plt
from pprint import pprint
import calendar
import re

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
    'cabi_active_members_monthly', 'cabi_monthly_multi_day_pases',
    'dless_users_jump', 'dless_users_lime', 'dless_users_mobike',
    'dless_users_ofo', 'dless_users_spin']

month_lst = {
    1: 'January', 2: 'Feburary', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
    12: 'December'}


def month_prep(mon):
    # convert float month digit to integer to string month name
    df[mon] = df[mon].astype(int)
    df[mon] = df[mon].map(month_lst)
    return df[mon]


class Data_Graph:
    # Class to draw different seaborn graphs. First step is init the dataframe
    def __init__(self, DATA):
        self.DATA = DATA

    def settings(self, columns, time):
        # list of columns to graph (y axis)
        self.columns = columns
        # Metric to graph by (x axis)
        self.time = time

    def utilization(self):
        # create utilization rates for cabi trip vars or dockless trip vars
        for x in self.columns:
            if re.match('cabi', x):
                self.DATA['{0}'.format(x.replace('trips', 'util'))] = (
                    self.DATA[x]/self.DATA['cabi_bikes_avail'])
                continue
            else:
                self.DATA['{0}'.format(x.replace('trips', 'util'))] = (
                    self.DATA[x]/self.DATA[x.replace('trips', 'bikes')])
        return self.DATA

    def grapher(self, axis, func):
        # pass in a list of matplotlib axis and a graphing module to plot ontop
        # of matplotlib figure. Little bit of sytle guides at the bottom for
        # graphs that use months on the x-axis.
        self.func = func
        self.axis = axis
        test = zip(self.columns, self.axis.flatten())
        for one, two in test:
            self.func(
                x=self.DATA[self.time], y=self.DATA[one], data=self.DATA,
                ax=two, showfliers=False, showmeans=True)
            if self.time == 'month':
                two.set_xticklabels(two.get_xticklabels(), rotation=45)


if __name__ == '__main__':
    # Loading the final database using a custom class to connect with AWS
    sys.path.append("..")
    conn = read_only_connect_aws()
    Full_Data = QueryTool(conn, 'final_db')
    df = Full_Data.basic()

    # Only looking at days with at least one dockless trip
    df = df[df['dless_trips_all'] != 0]

    # Open google drive connection
    dr = open_drive()

    # Duration of Trips
    f, axes = plt.subplots(2, 3, sharex='col', sharey='row',  figsize=(20, 10))
    first = Data_Graph(df)
    first.settings(distance, 'month')
    first.grapher(axes, sns.boxplot)
    all_in_one_save(
        "Trip Duration", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1db5i9U0QDnHO39lkNkDlYteG_Q5juY3q')

    # Average Monthly Trips
    f, axes = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(20, 10))
    first.settings(trips_agg, 'month')
    first.grapher(axes, sns.pointplot)
    all_in_one_save(
        "Avg Monthly Trips", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1db5i9U0QDnHO39lkNkDlYteG_Q5juY3q')

    # Utilization by Vendor
    f, axes = plt.subplots(2, 3, sharex='col', sharey='row', figsize=(20, 10))
    first = Data_Graph(df)
    first.settings(trips_gran, 'month')
    first.utilization()
    first.settings(df.filter(regex='util', axis=1), 'month')
    first.grapher(axes, sns.boxplot)
    all_in_one_save(
        "Utilization Vendor", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1db5i9U0QDnHO39lkNkDlYteG_Q5juY3q')

    # Active User by Vendor
    f, axes = plt.subplots(4, 2, sharex='col', sharey='row', figsize=(20, 10))
    first.settings(user_all, 'month')
    first.grapher(axes, sns.pointplot)
    all_in_one_save(
        "Active User Vendor", "C:/Users/Noah/Bikeshare-DC_Old/For Upload", dr,
        '1db5i9U0QDnHO39lkNkDlYteG_Q5juY3q')
