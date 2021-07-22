#! python3

from os import link
import sys, webbrowser,bs4, requests

searchTerms = input("Search: ")

print('Searching...')    # display text while downloading the search result page
url = ('https://google.com/search?q=' 'site%3Aw3schools.com+'+ searchTerms)
res = requests.get(url)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

import re

links =  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))

linkToOpen = links[0]
#print(linkToOpen.get("href"))

linkUrl = re.split(":(?=http)",linkToOpen["href"].replace("/url?q=",""))

linkUrl = linkUrl[0].split("&sa=")
print(linkUrl[0])

print('Opening', linkUrl[0])
webbrowser.open(linkUrl[0])