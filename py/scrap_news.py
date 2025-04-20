
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 뉴스 카테고리 딕셔너리
section_dict = {
    '최신뉴스': 'BreakingNews',
    '프리뷰': 'Preview',
    '스타 인터뷰': 'Interview',
    'KBO PHOTO': 'KboPhoto'
}

def get_news(section_name):
    m_id = section_dict.get(section_name)
    url = f'https://www.koreabaseball.com/MediaNews/News/{m_id}/List.aspx'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    news_list = []

    if res.ok:
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        if m_id == 'KboPhoto':
            tags = soup.select("ul.photoList li")
            for li in tags:
                a_tag = li.find('a')
                img_tag = li.find('img')
                title_tag = li.find('span')
                if a_tag and img_tag and title_tag:
                    news_list.append({
                        'title': title_tag.text.strip(),
                        'link': urljoin(url, a_tag['href']),
                        'img': urljoin(url, img_tag['src'])
                    })
        else:
            tags = soup.select("ul.boardPhoto li")
            for li in tags:
                a_tag = li.find('a')
                img_tag = li.find('img')
                title_tag = li.find('strong')
                if a_tag and img_tag and title_tag:
                    news_list.append({
                        'title': title_tag.text.strip(),
                        'link': urljoin(url, a_tag['href']),
                        'img': urljoin(url, img_tag['src'])
                    })
    return news_list

def get_sections():
    return list(section_dict.keys())