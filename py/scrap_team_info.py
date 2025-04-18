import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap_team_info() -> pd.DataFrame:
    """
    KBO 팀 데이터를 크롤링하여 DataFrame으로 반환하는 단일 함수.

    Args:
        url (str): 크롤링할 URL (KBO 팀 정보 페이지).
        headers (dict, optional): HTTP 요청 헤더 (기본값은 None).

    Returns:
        pd.DataFrame: 크롤링된 KBO 팀 정보 DataFrame.
    """
    
    # KBO 팀 정보 URL
    url = "https://www.koreabaseball.com/kbo/league/teaminfo.aspx"

    req_header = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    # 1. 웹 페이지 요청 및 HTML 가져오기
    response = requests.get(url)
    response.encoding = 'utf-8'  # 한글 인코딩 확인
    html = response.text

    # 2. BeautifulSoup을 사용한 HTML 파싱
    soup = BeautifulSoup(html, "html.parser")

    # 3. 팀 정보 테이블 찾기
    team_table = soup.find("table", class_="tData")  # 클래스 이름 확인 필요
    if not team_table:  # 테이블이 없는 경우 에러 처리
        print("팀 정보 테이블을 찾을 수 없습니다.")
    else:
        # 테이블에서 모든 행(tr)을 추출
        rows = team_table.find_all("tr")
        
        # 데이터를 저장할 리스트 초기화
        team_data = []

        # 4. 각 행에서 데이터 추출
        for row in rows[1:]:  # 첫 번째 행은 헤더이므로 건너뛰기
            cells = row.find_all("td")  # 열 데이터 추출
            
            # <td> 태그가 충분하지 않을 경우 건너뜀
            if len(cells) < 3:
                continue
            
            # 팀 정보 추출
            team_cell = cells[0]  # 첫 번째 열이 팀 정보
            team_name = team_cell.find("a").text.strip()  # 팀 이름 추출
            
            # 홈페이지에서 보이는 표가 전부가 아니라 각각 숨겨진 표가 더 있습니다
            # 특별한 예외: NC 다이노스는 열 번호가 다름
            if team_name == "NC 다이노스":
                founded_year = cells[4].text.strip()  # 창단연도 위치
                home_city = cells[5].text.strip()    # 연고지 위치
                team_site = cells[3].text.strip()
            else:
                founded_year = cells[3].text.strip()  # 창단연도 기본 위치
                home_city = cells[4].text.strip()    # 연고지 기본 위치
                team_site = cells[2].text.strip()
                
            # 데이터 추가
            team_data.append({
                "팀명": team_name,
                "창단연도": founded_year,
                "연고지": home_city,
                "구단 홈페이지": team_site
            })

    # 4. 리스트를 DataFrame으로 변환
    return pd.DataFrame(team_data)

scrap_team_info()