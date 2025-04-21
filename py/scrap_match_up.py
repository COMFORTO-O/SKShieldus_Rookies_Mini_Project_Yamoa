from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

def scrap_match_up():

    # Selenium 드라이버 실행
    driver = webdriver.Chrome()
    driver.get("https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx#none;")

    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, '..', 'csv')

    # 페이지 로드 대기
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "section")))
    time.sleep(2)

    # 모든 매치업 카드(li 태그) 가져오기
    all_li_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.game-list-n > li"))
    )

    # '경기예정' 텍스트가 있는 li 요소만 필터링
    match_up_li_list = [li for li in all_li_elements if '경기예정' in li.text]

    results_1 = []
    results_2 = []


    for li in match_up_li_list:
        try:
            # 경기시간과 구장 정보 추출
            match_up_time = li.find_element(By.CSS_SELECTOR, "div.top > ul > li:nth-of-type(3)")
            match_up_stadium = li.find_element(By.CSS_SELECTOR, "div.top > ul > li:nth-of-type(1)")
            
            match_time = match_up_time.text.strip()
            stadium = match_up_stadium.text.strip()

            # 카드 클릭 (상세정보 로딩)
            li.click()

            time.sleep(0.5)

            # 선발투수 정보 추출
            starting_pitchers = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.name-wrap > span.name"))
            )

            pitcher_1 = starting_pitchers[0].text.strip()
            pitcher_2 = starting_pitchers[1].text.strip()

            # 스탯 정보 추출 (AVG, WAR)
            td1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.tbl tr:nth-of-type(1) > td:nth-of-type(2)"))
            ).text.strip()
            td2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.tbl tr:nth-of-type(1) > td:nth-of-type(3)"))
            ).text.strip()
            td3 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.tbl tr:nth-of-type(2) > td:nth-of-type(2)"))
            ).text.strip()
            td4 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.tbl tr:nth-of-type(2) > td:nth-of-type(3)"))
            ).text.strip()

            time.sleep(0.5)








            # 팀 전력비교 탭 요소 저장 및 클릭
            team_power_omparison_tap = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.tab-depth2 > ul > li:nth-of-type(2)"))
            )
            team_power_omparison_tap.click()

            time.sleep(0.5)

            # 팀명 스크래핑
            team_name1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(1) > th > span"))
            ).text.strip()

            team_name2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(2) > th > span"))
            ).text.strip()

            
            # 팀 평균자책점, 타율 스크래핑
            team_avg1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(1) td:nth-of-type(3)"))
            ).text.strip()

            team_ba1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(1) td:nth-of-type(4)"))
            ).text.strip()

            team_avg2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(2) td:nth-of-type(3)"))
            ).text.strip()

            team_ba2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents table.tbl tbody tr:nth-of-type(2) td:nth-of-type(4)"))
            ).text.strip()

            time.sleep(0.5)





            # 라인업 분석 탭 요소 저장 및 클릭
            team_line_up_tap = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#gameCenterContents div.tab-depth2 ul li:nth-of-type(3) a"))
            )
            team_line_up_tap.click()




            # 팀 WAR 합산의 테이블세터 스크래핑
            war_statistics_tablesetter_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data > li:nth-of-type(1) div:nth-of-type(1) #txtLeftTableSetter"))
            ).text.strip()
            war_statistics_tablesetter_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data  li:nth-of-type(1) div:nth-of-type(2) #txtRightTableSetter"))
            ).text.strip()
            
            # 팀 WAR 합산의 중심타선 스크래핑
            war_statistics_core_lineup_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data > li:nth-of-type(2) div:nth-of-type(1) #txtLeftCleanUp"))
            ).text.strip()
            war_statistics_core_lineup_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data > li:nth-of-type(2) div:nth-of-type(2) #txtRightCleanUp"))
            ).text.strip()
            
            # 팀 WAR 합산의 하위타선 스크래핑
            war_statistics_lower_lineup_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data > li:nth-of-type(3) div:nth-of-type(1) #txtLeftBottom"))
            ).text.strip()
            war_statistics_lower_lineup_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.lineup-data > li:nth-of-type(3) div:nth-of-type(2) #txtRightBottom"))
            ).text.strip()




            # 포지션 스크래핑
            position_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-left.tbl-type04.w48p > table tbody tr td:nth-of-type(2)"))
            ).text.strip()
            position_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-right.tbl-type04.w48p  > table tbody tr td:nth-of-type(2)"))
            ).text.strip()

            # 선수명 스크래핑
            player_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-left.tbl-type04.w48p > table tbody tr td:nth-of-type(3)"))
            ).text.strip()
            player_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-right.tbl-type04.w48p > table tbody tr td:nth-of-type(3)"))
            ).text.strip()

            # WAR 스크래핑
            war_1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-left.tbl-type04.w48p > table tbody tr td:nth-of-type(4)"))
            ).text.strip()
            war_2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-right.tbl-type04.w48p > table tbody tr td:nth-of-type(4)"))
            ).text.strip()

            time.sleep(0.5)

            # 야구장별 홈팀 추론용 매핑
            stadium_home_team_map = {
                "잠실": "두산",
                "잠실": "LG",
                "문학": "SSG",
                "대구": "삼성",
                "고척": "키움",
                "대전(신)": "한화",
                "창원": "NC",
                "수원": "KT",
                "광주": "KIA",
                "부산": "롯데",
                "청주": "한화",
                "울산": "롯데",
                "사직" : "롯데"
            }

            # 결과 저장 1
            results_1.append({
                "경기시간": match_time,
                "야구장": stadium,

                "팀명1" : team_name1,
                "선발투수1": pitcher_1,
                "선발투수1 AVG": td1,
                "선발투수1 WAR": td2,
                "팀 AVG 1" : team_avg1,
                "팀 BA 1" : team_ba1,

                "팀명2" : team_name2,
                "선발투수2": pitcher_2,
                "선발투수2 AVG": td3,
                "선발투수2 WAR": td4,
                "팀 AVG 2" : team_avg2,
                "팀 BA 2" : team_ba2
            })

            for result_1_dict in results_1:
                stadium = result_1_dict['야구장']
                print(stadium)
                home_team = stadium_home_team_map.get(stadium)

                # 홈팀 / 원정팀 정리
                if result_1_dict['팀명1'] == home_team:
                    print("홈팀")
                else:

                    switched_data = {
                        "경기시간": match_time,
                        "야구장": stadium,

                        "팀명1": result_1_dict["팀명2"],  # 팀2 값을 팀1으로
                        "선발투수1": result_1_dict["선발투수2"],
                        "선발투수1 AVG": result_1_dict["선발투수2 AVG"],
                        "선발투수1 WAR": result_1_dict["선발투수2 WAR"],
                        "팀 AVG 1": result_1_dict["팀 AVG 2"],
                        "팀 BA 1": result_1_dict["팀 BA 2"],
                        
                        "팀명2": result_1_dict["팀명1"],  # 팀1 값을 팀2로
                        "선발투수2": result_1_dict["선발투수1"],
                        "선발투수2 AVG": result_1_dict["선발투수1 AVG"],
                        "선발투수2 WAR": result_1_dict["선발투수1 WAR"],
                        "팀 AVG 2": result_1_dict["팀 AVG 1"],
                        "팀 BA 2": result_1_dict["팀 BA 1"]
                    }
                    result_1_dict.update(switched_data)  # 업데이트된 데이터로 교체


            
            # 결과 저장 2
            results_2.append({
                "팀명 1" : team_name1,
                "팀1의 테이블세터 합산" : war_statistics_tablesetter_1,
                "팀1의 중심타선 합산" : war_statistics_core_lineup_1,
                "팀1의 하위타선" : war_statistics_lower_lineup_1,
                "팀1의 포지션": position_1,
                "팀1의 선수명": player_1,
                "팀1의 WAR": war_1,

                "팀명 2" : team_name2,
                "팀2의 테이블세터 합산" : war_statistics_tablesetter_2,
                "팀2의 중심타선 합산" : war_statistics_core_lineup_2,
                "팀2의 하위타선" : war_statistics_lower_lineup_2,
                "팀2의 포지션": position_1,
                "팀2의 선수명": player_2,
                "팀2의 WAR": war_2
            })


        except Exception as e:
            print(f"{e}")

    # 결과를 DataFrame으로 변환
    df_1 = pd.DataFrame(results_1)
    df_2 = pd.DataFrame(results_2)

    # 드라이버 종료
    driver.quit()

    df_1.to_csv(f'{csv_path}/scrap_match_up_main.csv', index=False, encoding='utf-8-sig')
    df_2.to_csv(f'{csv_path}/scrap_match_up_team.csv', index=False, encoding='utf-8-sig')

    return



# scrap_match_up()
