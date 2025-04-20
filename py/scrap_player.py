from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_hitter_data():
    url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    hitter_players = []

    for page in range(1, 4):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', class_='tData01 tt')

        for row in table.select('tbody > tr'):
            cols = row.find_all('td')
            if len(cols) > 1:
                hitter_players.append({
                    '순위': cols[0].text.strip(),
                    '선수명': cols[1].text.strip(),
                    '팀명': cols[2].text.strip(),
                    '타율': cols[3].text.strip(),
                    '경기': cols[4].text.strip(),
                    '타석': cols[5].text.strip(),
                    '타수': cols[6].text.strip(),
                    '득점': cols[7].text.strip(),
                    '안타': cols[8].text.strip(),
                    '2루타': cols[9].text.strip(),
                    '3루타': cols[10].text.strip(),
                    '홈런': cols[11].text.strip(),
                    '루타': cols[12].text.strip(),
                    '타점': cols[13].text.strip(),
                    '희생번트': cols[14].text.strip(),
                    '희생플라이': cols[15].text.strip()
                })

        try:
            next_button = driver.find_element(By.LINK_TEXT, str(page + 1))
            next_button.click()
            time.sleep(2)
        except:
            break

    driver.quit()
    return pd.DataFrame(hitter_players)


def scrape_pitcher_data():
    url = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/BasicOld.aspx'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    pitcher_players = []

    for page in range(1, 4):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', class_='tData01 tt')

        for row in table.select('tbody > tr'):
            cols = row.find_all('td')
            if len(cols) > 1:
                pitcher_players.append({
                    '순위': cols[0].text.strip(),
                    '선수명': cols[1].text.strip(),
                    '팀명': cols[2].text.strip(),
                    '평균자책점': cols[3].text.strip(),
                    '경기': cols[4].text.strip(),
                    '완투': cols[5].text.strip(),
                    '완봉': cols[6].text.strip(),
                    '승리': cols[7].text.strip(),
                    '패배': cols[8].text.strip(),
                    '세이브': cols[9].text.strip(),
                    '홀드': cols[10].text.strip(),
                    '승률': cols[11].text.strip(),
                    '타자수': cols[12].text.strip(),
                    '이닝': cols[13].text.strip(),
                    '피안타': cols[14].text.strip(),
                    '홈런': cols[15].text.strip(),
                    '볼넷': cols[16].text.strip(),
                    '사구': cols[17].text.strip(),
                    '삼진': cols[18].text.strip(),
                    '실점': cols[19].text.strip(),
                    '자책점': cols[20].text.strip()
                })

        try:
            next_button = driver.find_element(By.LINK_TEXT, str(page + 1))
            next_button.click()
            time.sleep(2)
        except:
            break

    driver.quit()
    return pd.DataFrame(pitcher_players)