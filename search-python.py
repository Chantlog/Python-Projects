#! python3
from os import link
import requests, sys, webbrowser, bs4

print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

print('https://google.com/search?q=' 'https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.package-snippet')

print(len(linkElems))

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)