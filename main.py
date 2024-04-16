import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.hltv.org/stats/teams/matches/7865/havu?startDate=2024-01-01&endDate=2024-12-31"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "proxy": "8.219.167.65"
}

r = requests.get(url=url, headers=headers)
# print(r.status_code)
# with open("index.html", "w") as file:
#     file.write(src)
# with open("index.html") as file:
#     src = file.read()
soup = BeautifulSoup(r.text, "lxml")
all_classes = ["group-2 first", "group-2", "group-1 first", "group-1"]
cyber_stat = []
for groups in all_classes:
    full = soup.find_all("tr", class_=f'{groups}')
    for i in full:
        team = soup.find('span', class_='context-item-name').text
        data = i.find('td', class_='time').text
        match = i.find('td', class_='gtSmartphone-only').text
        opponent = i.find_all('a')[3].text
        map_map = i.find('td', class_='statsMapPlayed').text
        result = i.find('span', class_='statsDetail').text
        w_l = i.find_all('td')[6].text
        cyber_stat.append([team, data, match, opponent, map_map, result, w_l])
headers = ['team', 'data', 'match', 'opponent', 'map_map', 'result', 'w_l']
df = pd.DataFrame(cyber_stat, columns=headers)
csv_name = 'cyber_stat_havu_24' + '.csv'
df.to_csv(csv_name)

