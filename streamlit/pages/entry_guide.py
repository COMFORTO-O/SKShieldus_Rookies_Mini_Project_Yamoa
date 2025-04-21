import streamlit as st
import sys
import pandas as pd
import sys
import os

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../components")

from navbar import show
from scrap_news import get_news, get_sections
from scrap_team_info import scrap_team_info

# 네브바 보이기
show()

# 페이지 제목 CSS
st.markdown("""
    <style>
    .section-wrapper {
        border-bottom: 2px solid #d3d3d3;
        padding-bottom: 6px;
        margin: 20px;
    }
    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #333;
        text-align: left;
        margin: 0;
    }
    .blank {
        margin: 20px;        
    }
    </style>
""", unsafe_allow_html=True)

# ------------ 뉴스 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">주요 뉴스</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
categories = get_sections()

selected_category = None
cols = st.columns(len(categories))
for i, category in enumerate(categories):
    if cols[i].button(category):
        selected_category = category

# 뉴스 불러오기
if selected_category:
    news_list = get_news(selected_category)
    st.markdown(f"### {selected_category}")
else:
    news_list = get_news('최신뉴스')
    st.markdown(f"### 최신뉴스")

# 뉴스 3개씩 정렬 + 이미지, 제목에 링크 + 이미지 사이즈 통일
for i in range(0, len(news_list), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(news_list):
            news = news_list[i + j]
            with cols[j]:
                # 이미지에 링크
                if 'img' in news:
                    st.markdown(f'''
                        <a href="{news['link']}" target="_blank">
                            <img src="{news['img']}" style="width:100%; height:180px; object-fit:cover; border-radius:10px;" />
                        </a>
                    ''', unsafe_allow_html=True)
                # 제목에도 링크
                st.markdown(f'''
                    <p style='text-align:center; font-weight:bold; font-size:16px'>
                        <a href="{news['link']}" target="_blank" style="color:inherit; text-decoration:none;">
                            {news['title']}
                        </a>
                    </p>
                ''', unsafe_allow_html=True)

# ------------ 팀 정보 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">구단 소개</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
team_df = scrap_team_info()
st.table(team_df)
# st.dataframe(team_df, use_container_width=True)