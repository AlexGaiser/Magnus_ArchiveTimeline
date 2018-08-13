#! python3 

#Magnus Archive Timeline, RSS Feed Parser
#this module gets the rss feed and extracts the data we want
from pyPodcastParser.Podcast import Item, Podcast

from bs4 import BeautifulSoup

import re
import requests as re
import dateTMA as dt # function convert()
url = 'https://rss.acast.com/themagnusarchives'
res = re.get(url)

res.raise_for_status()
text = res.text
soup = BeautifulSoup(text, "xml")

# print(soup)
description = soup.findAll('itunes:subtitle')#this finds all the summaries which should contain the data we need. 
title = soup.findAll('title')
#the statement giver
# we are looking to extract the statement number


#convert the statement number to a regular date. This will be handled by the statement conversion module

for i in title:
	print(i.get_text)