from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

def scrape_team_rank():
    driver = webdriver.Chrome()
    driver.get("https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', class_='tData')

    team_data = []

    for row in table.select('tbody > tr'):
        cols = row.find_all('td')
        if len(cols) > 1:
            rank = cols[0].text.strip()
            team = cols[1].text.strip()
            plays = int(cols[2].text.strip())
            win = cols[3].text.strip()
            lose = int(cols[4].text.strip())
            draw = int(cols[5].text.strip())
            win_rate = cols[6].text.strip()
            draw_rate = int(round(draw / plays, 3) * 1000)
            lose_rate = int(round(lose / plays, 3) * 1000)

            team_info = {
                '순위': rank,
                '팀명': team,
                '경기': plays,
                '승': win,
                '패': lose,
                '무': draw,
                '승률': win_rate
            }
            team_data.append(team_info)

    driver.quit()

    df = pd.DataFrame(team_data)
    df['패배율'] = round(df['패']/df['경기'].astype(float), 3)

    if not os.path.exists('data'):
        os.mkdir('data')

    df.to_csv('../../csv/scrap_team_rank.csv', index=False)


def scrape_team_avg():
    driver = webdriver.Chrome()
    driver.get("https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', class_='tData tt')

    team_data = []

    for row in table.select('tbody > tr'):
        cols = row.find_all('td')
        if len(cols) > 1:
            rank = cols[0].text.strip()
            team = cols[1].text.strip()
            avg = cols[2].text.strip()

            team_info = {
                '순위': rank,
                '팀명': team,
                '타율': avg
            }
            team_data.append(team_info)

    driver.quit()

    df = pd.DataFrame(team_data)

    df.to_csv('../../csv/scrap_team_avg.csv', index=False)


def scrape_team_vs():
    driver = webdriver.Chrome()
    driver.get("https://www.koreabaseball.com/Record/TeamRank/TeamRank.aspx")

    wait = WebDriverWait(driver, 10)
    year_dropdown = wait.until(EC.presence_of_element_located((By.ID, "cphContents_cphContents_cphContents_ddlYear")))

    select = Select(year_dropdown)
    select.select_by_visible_text("2024")

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    vs_team_div = soup.find("div", id="cphContents_cphContents_cphContents_pnlVsTeam")
    table = vs_team_div.find('table', class_='tData')

    team_data = []

    for row in table.select('tbody > tr'):
        cols = row.find_all('td')
        if len(cols) > 1:
            team = cols[0].text.strip()
            kia = cols[1].text.strip()
            samsung = cols[2].text.strip()
            lg = cols[3].text.strip()
            doosan = cols[4].text.strip()
            kt = cols[5].text.strip()
            ssg = cols[6].text.strip()
            lotte = cols[7].text.strip()
            hanwha = cols[8].text.strip()
            nc = cols[9].text.strip()
            kiwoom = cols[10].text.strip()
            summary = cols[11].text.strip()

            team_info = {
                '팀명': team,
                'KIA': kia,
                '삼성': samsung,
                'LG': lg,
                '두산': doosan,
                'KT': kt,
                'SSG': ssg,
                '롯데': lotte,
                '한화': hanwha,
                'NC': nc,
                '키움': kiwoom,
                '합계': summary
            }
            team_data.append(team_info)

    driver.quit()

    df = pd.DataFrame(team_data)

    df.to_csv('../../csv/scrap_team_last_year.csv', index=False)


def calculate_win_rate():
    df_team = pd.read_csv('../../csv/scrap_team_last_year.csv')

    df_team = df_team.drop(columns=['합계'])

    team_dict = []

    for idx, row in df_team.iterrows():
        team_name = row['팀명']
        team_data = {'팀명': team_name}

        for col in df_team.columns[1:]:  # 팀명을 제외한 상대 팀들
            value = row[col]
            if '-' in str(value):
                win, lose, draw = map(int, value.split('-'))
                win_rate = int(win) / int(win + lose + draw)
                team_data[col] = win_rate
            else:
                team_data[col] = '■'  # 자기 자신은 '■'로 표시되므로 제외하거나 None 처리

        team_dict.append(team_data)

    df = pd.DataFrame(team_dict)

    df.to_csv('../../csv/scrap_team_win_rate_last_year.csv', index=False)
