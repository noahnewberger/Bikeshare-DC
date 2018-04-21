import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

pre_url = 'https://www.baseball-reference.com/teams/WSN/'
post_url = '-schedule-scores.shtml'

#Inititialize blank dataframe
nats_sched = pd.DataFrame()

#for loop for year 2010-2018
for i in range(2010, 2019):
    # Define correct URL for year in range
    url = pre_url + str(i) + post_url
    #Save get request as r
    r = requests.get(url)
    #Use beautifulsoup?
    soup = BeautifulSoup(r.text, "lxml")
    #Extract schedule table from HTML
    schedule =  soup.find('div', attrs={'class':'overthrow table_container'})
    #Create dataframe
    schedule = pd.read_html(str(schedule))[0]
    #Drop extra header rows embeded in dataframe
    schedule = schedule[schedule['Gm#'] != 'Gm#']
    #Remove parentheses and their contents from Date column
    schedule['Date'] = schedule['Date'].str.replace(r"\(.*\)","")
    #Add the year to the dates in date
    schedule['Date'] = schedule['Date'] +", " + str(i)
    #Append games from current iteration (season) to nats_sched dataframe
    nats_sched = nats_sched.append(schedule)


#Name unnamed columns in dataframe
nats_sched.rename(columns = {'Unnamed: 2':'BoxScore', 'Unnamed: 4':'Home/Away'}, inplace=True)

print(nats_sched)
