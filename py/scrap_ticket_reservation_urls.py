# 8. 티켓 예매처 스크래핑

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrap_ticket_reservation_urls():

    url = "https://www.koreabaseball.com/Kbo/League/Map.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }

    # url로 html을 paersing 함, headers는 사용자가 사람이라는 것을 인증하기 위함
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # <td> 태그 전체 수집
    td_tags = soup.select('td')

    # td_tags의 <a> 태그 전체 수집
    a_tags = [a for td in td_tags for a in td.find_all('a')]

    # base_url은 상대경로로 되어 있는 url (페이지 <a> 태그의 href 속성)을
    # urljoin으로 결합하여 절대경로로 만드는 변수
    base_url = 'https://www.example.com'
    absolute_hrefs = [urljoin(base_url, a.get('href')) for a in a_tags if a.get('href')]

    # 열 개수 - 티켓링크, 인터파크, 구단 자체매매*2
    num_columns = 4

    # 절대경로 리스트를 행 단위로 잘라서 리스트로 변환
    data = [absolute_hrefs[i:i + num_columns] for i in range(0, len(absolute_hrefs), num_columns)]

    # 열 이름 설정
    columns = ['티켓링크', '인터파크', '자이언트', 'nc다이노스']

    # 데이터프레임 생성
    ticket_reservation_url = pd.DataFrame(data, columns=columns)

    ticket_reservation_url.to_csv('./csv/scrap_ticket_reservation_urls.csv', index=False, encoding='utf-8-sig')

    # 출력
    ticket_reservation_url