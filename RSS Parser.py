#! python3 

#Magnus Archive Timeline, RSS Feed Parser
#this module gets the rss feed and extracts the data we want


#todo:

#get title of episode //done
#get statement giver
#get case number
#run case number through conversion function



from pyPodcastParser.Podcast import Item, Podcast

from bs4 import BeautifulSoup
import filemaker as fm
import re, csv
import requests as req
import dateTMA as dt # function convert()
url = 'https://rss.acast.com/themagnusarchives'
res = req.get(url)


# def soupfind(search,var):
#     var = soup.findAll(search)

fm.filemaker('TMA_Cases','.csv', 'Case#,Title, \n')

res.raise_for_status()
text = res.text
soup = BeautifulSoup(text, "xml")

# print(soup)
title = soup.findAll('title')
#the statement giver
# we are looking to extract the statement number
description = soup.findAll('description')
#convert the statement number to a regular date. This will be handled by the statement conversion module
item = soup.findAll('item')
summary = soup.findAll('itunes:summary')
testcase = '''['<p>Case #9982211</p>\n<p>Statement of Joshua Gellespie regarding his time in the possession of an apparently empty wooden casket.</p>\n<p>…</p>\n<p>For the duration of launch we will be releasing three episodes a week instead of our normal weekly release schedule. We hope you enjoy the extra terror…</p>\n<p>Be sure to subscribe using your podcast software of choice to get every episode automatically downloaded  to your device. It’s more convenient for you and really helps us out. Even better, leave us a review. The more reviews we get, the more people listen and the more we can make!</p>\n<p>Like what you’re hearing? Let us know:<br />\nTweet us at @theRustyQuill, drop us an email at mail@RustyQuill.com or comment on our dedicated Forums available at www.RustyQuill.com.</p>\n<p>For more information visit RustyQuill,com.</p>']
['<p>Case #0122204</p>\n<p>Statement of Nathan Watts, regarding an encounter on Old Fishmarket Close, Edinburgh .</p>\n<p>…</p>\n<p>The Magnus Archives are now open…</p>\n<p>Join Head Archivist Jonathan Sims as he begins his work transcribing the archives of the Magnus Institute. An organisation dedicated to the investigation of the esoteric and weird.</p>\n<p>For the duration of launch we will be releasing three episodes a week instead of our normal weekly release schedule. We hope you enjoy the extra terror…</p>\n<p>Be sure to subscribe to us on your podcast software of choice to get every episode automatically downloaded straight to your device. It’s more convenient for you and really helps us out. Even better, leave us a review! The more we get the more programming we can make!</p>\n<p>Like what you’re hearing? Let us know:<br />\nTweet us at @theRustyQuill, drop us an email at mail@RustyQuill.com or comment on our dedicated Forums available at www.RustyQuill.com.</p>\n<p>For more 
'''

caseRe = re.compile(r'\d\d\d\d\d\d\d')
case = caseRe.search(testcase)
print(case.group())

List = []
sumlist =[]
caselist = []
for i in description:
    i = i.contents
    i = i[0]
    try:
        caseRe = re.compile(r'\d\d\d\d\d\d\d')
        
        # caseRe = re.compile()
        case = caseRe.search(i)
        print(case.group())
        date = dt.convert(case.group())
        caselist.append(date)
    except:
       print('no case number ')
       caselist.append('no case number')

for i in summary:
    i = i.contents
    i = i[0]
    sumlist.append(i)

for i in title: #gets the dates from the RSS feed, iterates over the feed 
    i = i.contents
    i = i[0]
    List.append(i)


print(List)
print(caselist)

print(len(List))
print(len(caselist))
print(len(sumlist))

with open ('TMA_Cases.csv', "a", newline = '', encoding='utf-8') as Output_CSV:
    csvWriter = csv.writer(Output_CSV)
    csvWriter.writerow(List)
    csvWriter.writerow(caselist)
    csvWriter.writerow(sumlist)


#print(List)# this currently works perfectly, a full list of every episode title