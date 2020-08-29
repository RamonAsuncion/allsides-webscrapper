from bs4 import BeautifulSoup
import requests
from time import sleep
from rich.progress import track


url = "https://www.allsides.com/news-source/abc-news-media-bias"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

table = soup.select('tbody tr')


# website = soup.select(
#     'body > div.full-news-source > div > div > div.span4 > div > ul > li:nth-child(1)')
# print(website)

# website = soup.select('div.span4 > div > ul > li:nth-child(1)')
# print(website)

website = soup.find('div', {'class': 'dynamic-grid'})
link = website.find('a')['href']
print(link)

sleep(10)
print("10 seconds have passed")

# <a href="http://abcnews.go.com/" target="_blank" alt="ABC News (Online)" title="ABC News (Online)" rel="noopener">


# fullTable = []  # empty list

# for row in table:
#     f = dict()
#     f['linkToNewsInfo'] = 'https://www.allsides.com' + \
#         row.select_one('.source-title a')['href']

#     fullTable.append(f)

# sleep(10)
# print("continue on testing 10 seconds have passed")

# for d in track(range(100), description="Parsing..."):
#     r = requests.get(f['linkToNewsInfo'])
#     soup = BeautifulSoup(source.content, 'lxml')

#     try:
#         websiteLink = website = soup.select_one('a')['href']
#         f['News Source Site'] = websiteLink
#     except TypeError:
#         pass
# fullTable.append(f)

# print(fullTable[0])
