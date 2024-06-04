# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:46:34 2023

@author: MingyangWang

"""

import praw
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import os

option = input("Which party: ")
if option == "D":
    fileC = open(
        "E:\\01_NYU\\2023\\2023 Spring Research\\politicsProject\\politicsProjectCharles\\candidateList\\democrateList.txt",
        "r")
    candidates = fileC.readlines()
    fileC.close()
    party = "democrates"
    print("end")

elif option == "R":
    fileC = open(
        "E:\\01_NYU\\2023\\2023 Spring Research\\politicsProject\\politicsProjectCharles\\candidateList\\RepublicanList.txt",
        "r")
    candidates = fileC.readlines()
    fileC.close()
    
    party = "republicans"
    print("end")
    
'''
for name in candidates:
    name = name.strip()
    os.mkdir("E:\\01_NYU\\2023\\2023 Spring Research\\politicsProject\\politicsProjectCharles\\" + party + "\\" + name)
'''

reddit = praw.Reddit(
    client_id="y3gGwSYwfgnuzlEWToPESw",
    client_secret="yKIIhHrAb_OYHhc2vmEU73zqJnUwug",
    username="charles2739",
    password="Wmy2022offer@",
    user_agent="analyticsResearch",
    check_for_async=False
     )

# change the date every time before run the programD
target_date = datetime(2024, 6, 3)

 # utc_now = datetime.utcnow()
# utc_start_time = utc_now - timedelta(days=1)

start_time = datetime(target_date.year, target_date.month, target_date.day)
end_time = start_time + timedelta(days=1)

utc_start_time = int(start_time.timestamp())
utc_end_time = int(end_time.timestamp())

time_range = 'week'

# print(reddit.user.me())

for candidate in candidates:
    a = reddit.subreddit("all")
    
    candidate = candidate.strip()
    b = a.search(candidate, time_filter=time_range,  sort = 'new', syntax = 'lucene', limit = 1000)
    print(candidate)
    mylist = []
    
    for i in b:
        
        created_datetime = dt.datetime.fromtimestamp(i.created_utc)

        # Check if the submission is within the desired date range
        if start_time <= created_datetime < end_time:
            print(created_datetime)
            # time = dt.datetime.utcfromtimestamp(i.created_utc).strftime('%m-%d-%Y')
            time = created_datetime
            timeFormat = time.strftime('%m-%d-%Y')
            mylist.append([time, i.title, i.score, i.upvote_ratio, i.url])
    
    data = pd.DataFrame(mylist, columns = ['date', 'post title', 'score', 'upvote_ratio', "url"])
    filename = "E:\\01_NYU\\2023\\2023 Spring Research\\politicsProject\\politicsProjectCharles\\" + party+"\\" + candidate+"\\"+ timeFormat+".csv"
    data.to_csv(filename, mode = 'a')