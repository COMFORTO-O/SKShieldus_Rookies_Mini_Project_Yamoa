# 4-1. 경기 정보 데이터 (팀, 구장, 날짜, 시간) 스크래핑
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def scrap_preview_urls():

    # Chrome 드라이버를 새로 설치하여 Chrome 실행
    driver = webdriver.Chrome()
    driver.get("https://www.koreabaseball.com/Schedule/Schedule.aspx")

    # 페이지가 로드될 때까지 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # 텍스트가 '프리뷰'인 a태그 추출
    # 해당 사이트는 동적 페이지이기 때문에 동적 웹 스크래핑 라이브러리인 selenium을 사용해야 함
    a_tag_preview_text = driver.find_elements(By.XPATH, "//a[normalize-space(text())='프리뷰']")


    # URL을 저장할 빈 리스트 생성
    preview_url_list = []

    # 프리뷰 URL 추출
    for index, link in enumerate(a_tag_preview_text):
        href = link.get_attribute('href')
        preview_url_list.append(href)

    df = pd.DataFrame(preview_url_list, columns=['url'])
    df.to_csv('./csv/scrap_preview_urls.csv', index=False, encoding='utf-8-sig')

    # Chrome 닫기
    driver.quit()

    # 출력
    df