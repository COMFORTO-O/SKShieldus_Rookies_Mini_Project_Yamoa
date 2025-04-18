# 4-2. 팀 기록 데이터 (순위, 팀명, 타율, 경기, 타석, 타수, 득점, 안타, 2루타, 3루타, 홈런, 투타, 타점, 희생번트, 희생플라이) 스크래핑

import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrap_team_record():

    url = "https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }

    # url로 html을 paersing 함, headers는 사용자가 사람이라는 것을 인증하기 위함
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # <td> 태그 전체 수집
    td_tags = soup.find_all('td')

    # td에서 텍스트만 추출
    td_text = [td.get_text(strip=True) for td in td_tags]

    # 열 개수 (한 팀당 데이터 수)
    # 순위 + 팀명 + AVG + G + PA + AB + R + H + 2B + 3B + HR + TB + RBI + SAC + SF
    num_columns = 15

    # td 리스트를 행 단위로 잘라서 리스트로 변환
    data = [td_text[i:i + num_columns] for i in range(0, len(td_text), num_columns)]

    # 열 이름 설정
    columns = ['순위', '팀명', '타율', '경기', '타석', '타수', '득점', '안타', '2루타', '3루타', '홈런', '투타', '타점', '희생번트', '희생플라이']

    # 데이터프레임 생성
    team_info_df = pd.DataFrame(data, columns=columns)
    team_info_df = team_info_df[team_info_df['순위'] != '합계']

    # 데이터프레임 저장
    team_info_df.to_csv('./csv/scrap_team_record.csv', index=False, encoding='utf-8-sig')

    # 출력
    print(team_info_df)
