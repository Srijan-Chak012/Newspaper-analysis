import requests
import html5lib
import json
import pprint
from bs4 import BeautifulSoup


def get_day_links(date):
    url = 'https://www.thehindu.com/archive/print/' + date + '/'
    r = requests.get(url)
    # print(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    archive_lists = soup.findAll('ul', class_='archive-list')
    links = []

    for al in archive_lists:
        hrefs = al.findAll('a')
        # print(hrefs)
        for href in hrefs:
            link = href['href']
            links.append(link)
    return links


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    t_div = soup.findAll(class_='article')
    title = t_div[0].find_all(class_='title')[0].get_text().strip()
    body = t_div[0].select("[id*='content-body-']")
    body_t = ""

    for p in body[0].find_all('p'):
        body_t = body_t + p.get_text() + "\n"

    return title, body_t


# get_data('https://www.thehindu.com/todays-paper/modi-asks-states-to-prepare-for-ramping-up-economic-activity/article31562091.ece')
l = get_day_links('2020/12/12')
storage = []
i = 0
for link in l:
    print(str(i+1)+"/"+str(len(l)))
    try:
        t, b = get_data(link)
        storage.append({})
        storage[i]["title"] = t
        storage[i]["body"] = b
        # pprint.pprint(storage)
        i = i + 1
    except:
        print("Got an error")
        continue

with open("output2.json", "w") as f:
    json.dump(storage, f, indent=6)