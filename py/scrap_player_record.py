# 4-3. 선수 기록 데이터 (순위, 선수명, 팀명, 타율, 경기, 타석, 타수, 득점, 안타, 2루타, 3루타, 홈런, 투타, 타점, 희생번트, 희생플라이) 스크래핑

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrap_player_record():

    # Chrome 브라우저 설정 (headless 모드도 가능)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 브라우저 안 띄우려면 주석 해제
    driver = webdriver.Chrome(options=options)


    def get_player_record_data(url, position): 
        # Chrome 브라우저 설정 및 실행 (함수 내부로 이동)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

        # KBO 타자 기록 페이지 열기
        players_url = url
        driver.get(players_url)

        # 대기 객체 (웹 요소가 로드될 때까지 대기)
        wait = WebDriverWait(driver, 7)

        # 데이터 저장 리스트
        all_rows = []

        # 페이지 번호가 1부터 시작한다고 가정
        for page in range(1, 10):  # 예: 1~3페이지 수집
            print(f"{page}페이지 수집 중...")

            # 테이블이 로드될 때까지 대기
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

            # 현재 페이지의 테이블에서 tr 추출
            table = driver.find_element(By.TAG_NAME, "tbody")
            rows = table.find_elements(By.TAG_NAME, "tr")

            # 테이블에서 각 행의 데이터를 추출
            for row in rows:
                tds = row.find_elements(By.TAG_NAME, "td")
                row_data = [td.text for td in tds]
                if row_data:  # 빈 줄 제외
                    all_rows.append(row_data)

            # 다음 페이지로 넘어가기
            try:
                next_page_btn = driver.find_element(By.LINK_TEXT, str(page + 1))  # 페이지 버튼을 클릭
                next_page_btn.click()
                time.sleep(1.5)
            except:
                print(f"{page + 1} 페이지 없음.")
                break

        # 열 이름 정의
        if position == "타자 데이터" :
            columns = ['순위', '선수명', '팀명', '타율', '경기', '타석', '타수', '득점', '안타', '2루타', '3루타', '홈런', '투타', '타점', '희생번트', '희생플라이']
        else:
            columns = ['순위', '선수명', '팀명', '평균자책점', '경기', '승리', '패배', '세이브', '홀드', '승률', '이닝', '피안타', '홈런', '볼넷', '사구', '삼진', '실점', '자책점', '이닝당 출루허용률']


        # DataFrame 생성
        df = pd.DataFrame(all_rows, columns=columns)

        # "합계" 행 제거
        df = df[df['순위'] != '합계']

        if position == "타자 데이터":
            df.to_csv('./csv/scrap_batter_record.csv', index=False, encoding='utf-8-sig')
        else:
            df.to_csv('./csv/scrap_bowler_record.csv', index=False, encoding='utf-8-sig')

        # 브라우저 종료
        driver.quit()

        # 결과 출력
        print(position, df)
        return

    print(get_player_record_data("https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT", "타자 데이터"))
    print(get_player_record_data("https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx", "투수 데이터"))

