from bs4 import BeautifulSoup
import requests
from time import sleep
from rich.progress import track


url = "https://www.allsides.com/news-source/abc-news-media-bias"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

table = soup.select('tbody tr')

fullTable = []  # empty list

for row in table:
    f = dict()
    f['linkToNewsInfo'] = 'https://www.allsides.com' + \
        row.select_one('.source-title a')['href']

    fullTable.append(f)

sleep(10)
print("continue on testing 10 seconds have passed")

for d in track(range(100), description="Parsing..."):
    r = requests.get(f['linkToNewsInfo'])
    soup = BeautifulSoup(source.content, 'lxml')

    try:
        websiteLink = website = soup.select_one('a')['href']
        f['News Source Site'] = websiteLink
    except TypeError:
        pass
fullTable.append(f)

print(fullTable[0])
