from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=800,700")
chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")

driver = webdriver.Chrome(options=chrome_options, service=service)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
})

URLS = [
    '/stats/teams/9881/rooster?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/9455/imperial?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/6673/nrg?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7532/big?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5378/virtuspro?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    "/stats/teams/7020/spirit?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2",
    '/stats/teams/9215/mibr?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11948/nouns?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11861/aurora?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12376/m80?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/6248/themongolz?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4991/fnatic?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/6667/faze?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7176/red-canids?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4914/3dmax?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11811/monte?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12183/the-witchers?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4773/pain?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5752/cloud9?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2'
    '/stats/teams/12534/boss?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2'
    '/stats/teams/11251/eternal-fire?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12334/preasy?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11164/into-the-breach?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11837/fluxo?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7175/heroic?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4494/mouz?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10567/saw?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7234/endpoint?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10577/sinners?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11176/mouz-nxt?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8038/party-astronauts?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5995/g2?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4863/tyloo?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12591/koi?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11883/9-pandas?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12468/legacy?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8113/sharks?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11641/metizport?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4608/natus-vincere?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7441/eclot?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10333/sangal?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5996/tsm?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    "/stats/teams/10695/sampi?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2",
    '/stats/teams/12394/betboom?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11668/mindfreak?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8135/forze?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11523/zero-tenacity?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10973/anonymo?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12289/espionage?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4411/ninjas-in-pyjamas?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5005/complexity?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12524/pera?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/9996/9z?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8637/sprout?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8840/lynn-vision?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11419/ecstatic?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8297/furia?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12257/wildcard?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11241/b8?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12474/alliance?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11982/ikla?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10278/9ine?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10459/arcred?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4501/alternate-attax?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12000/500?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/4869/ence?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12527/guild-eagles?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12455/vantage?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12677/galorys?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10894/case?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/9806/apeks?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12426/passion-ua?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/9928/gamerlegion?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12009/permitta?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12233/solid?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12144/bestia?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/6902/godsent?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11768/oddik?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10905/pge-turow?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/5479/mythic?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12041/the-chosen-few?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/7187/nexus?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/10831/entropiq?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/11737/eyeballers?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/8574/w7m?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
    '/stats/teams/12065/flamengo?startDate=2023-10-12&endDate=2024-04-12&csVersion=CS2',
]
CREW_BOX = ['/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[10]/div[1]/div/a',
            '/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[10]/div[2]/div/a',
            '/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[10]/div[3]/div/a',
            '/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[10]/div[4]/div/a',
            '/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[10]/div[5]/div/a']
ALL_CLASSES = ["group-2 first", "group-2", "group-1 first", "group-1"]


def main():
    driver.get("https://www.hltv.org/stats/teams?csVersion=CS2&startDate=2023-10-12&endDate=2024-04-12")
    driver.find_element('xpath', '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    sleep(5)
    stat_team = []
    stat_crew = []
    stat_games = []
    for i in URLS:
        try:
            driver.get('https://www.hltv.org' + i)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            sleep(5)
            team = soup.find('span', class_='context-item-name').text
            maps_played = soup.find_all('div', class_='col standard-box big-padding')[0].find('div', class_='large-strong').text
            wins_draws_lose = soup.find_all('div', class_='col standard-box big-padding')[1].find('div', class_='large-strong').text
            total_kills = soup.find_all('div', class_='col standard-box big-padding')[2].find('div', class_='large-strong').text
            total_death = soup.find_all('div', class_='col standard-box big-padding')[3].find('div', class_='large-strong').text
            k_d_ratio = soup.find_all('div', class_='col standard-box big-padding')[5].find('div', class_='large-strong').text
        except Exception:
            continue
        stat_team.append(
            {
                'team': team,
                'maps_played': maps_played,
                'wins_draws_lose': wins_draws_lose,
                'total_kills': total_kills,
                'total_death': total_death,
                'k_d_ratio': k_d_ratio
            }
        )
        print([team, maps_played, wins_draws_lose, total_kills, total_death, k_d_ratio])
        for ii in CREW_BOX:
            try:
                driver.find_element('xpath', ii).click()
                sleep(3)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                name = soup.find('span', class_='context-item-name').text
                total_kills_from_crew = soup.find_all('div', class_='stats-row')[0].find_all('span')[1].text
                headshots_from_crew = soup.find_all('div', class_='stats-row')[1].find_all('span')[1].text
                total_death_from_crew = soup.find_all('div', class_='stats-row')[2].find_all('span')[1].text
                k_d_ratio_from_crew = soup.find_all('div', class_='stats-row')[3].find_all('span')[1].text
                maps_played_from_crew = soup.find_all('div', class_='stats-row')[6].find_all('span')[1].text
                rating_2_0_from_crew = soup.find_all('div', class_='stats-row')[13].find_all('span')[1].text
                driver.back()
            except Exception:
                continue
            print([name, total_kills_from_crew, headshots_from_crew, total_death_from_crew, k_d_ratio_from_crew, maps_played_from_crew, rating_2_0_from_crew])
            stat_crew.append(
                {
                    'team': team,
                    'name': name,
                    'total_kills_from_crew': total_kills_from_crew,
                    'headshots_from_crew': headshots_from_crew,
                    'total_death_from_crew': total_death_from_crew,
                    'k_d_ratio_from_crew': k_d_ratio_from_crew,
                    'maps_played_from_crew': maps_played_from_crew,
                    'rating_2_0_from_crew': rating_2_0_from_crew
                }
            )
        driver.find_element('xpath', '/html/body/div[2]/div[5]/div[2]/div[1]/div[2]/div[3]/div/div/a[2]').click()
        sleep(3)
        for groups in ALL_CLASSES:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            full = soup.find_all("tr", class_=f'{groups}')
            for j in full:
                opponent = j.find_all('a')[3].text
                map_map = j.find('td', class_='statsMapPlayed').text
                result = j.find('span', class_='statsDetail').text
                w_l = j.find_all('td')[6].text
                print(opponent, map_map, result, w_l)
                stat_games.append(
                    {
                        'team': team,
                        'opponent': opponent,
                        'map_map': map_map,
                        'result': result,
                        'w_l': w_l
                    }
                )
    team_df = pd.DataFrame(stat_team)
    crew_df = pd.DataFrame(stat_crew)
    game_df = pd.DataFrame(stat_games)
    df = pd.concat([team_df, crew_df, game_df], axis=1)
    csv_name = 'cyber_stat_new_test' + '.csv'
    df.to_csv(csv_name, index=False)


if __name__ == '__main__':
    main()







