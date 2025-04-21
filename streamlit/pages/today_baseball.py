import streamlit as st
import sys
import pandas as pd
from PIL import Image
import os

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../../csv")
sys.path.append("../jupyter/scraping")
sys.path.append("../components")

from navbar import show
from plt_OddsofWinning import plt_OddsofWinning
from ml_winrate import RF_winrate
from dataset_matchup import dataset_matchup
from scrap_match_up import scrap_match_up
from plt_match_up import plt_match_up 
# 네브바 보이기
show()

# 스타일 설정
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
    div.stButton > button {
        white-space: pre-wrap;
        height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# ------------ 제목 ------------

st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">오늘의 승부 예측</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ------------ 예측 및 데이터 로딩 ------------

# scrap_match_up() # 오늘의 경기 정보 스크래핑, home away 순서 조정정
dataset_matchup()  # 경기 정보 데이터셋 생성
RF_winrate() # 머신러닝 예측 수행 → csv 파일 생성
# 경기 정보 파일 로드
matches = pd.read_csv(f"../../csv/scrap_match_up_main.csv", encoding='utf-8-sig')

# # ------------ 버튼 UI ------------

st.markdown("## 📊 오늘의 승부 예측 결과를 확인하세요!")

# 동적으로 컬럼 수 생성 (5개 단위씩 묶기)
selected_match = None
cols = st.columns(min(len(matches), 5))

for i, row in matches.iterrows():
    col = cols[i % 5]
    with col:
        match_label = f"{row['팀명1']}  vs  {row['팀명2']}\n📍 {row['야구장']}\n 🕒 {row['경기시간']}"

        if st.button(match_label, key=f"match_{i}", use_container_width=True):
            selected_match = (row['팀명1'], row['팀명2'])
            

# # ------------ 머신러닝 승부 예측 시각화 결과 출력 ------------


if selected_match:
    home_team, away_team = selected_match
    st.markdown(f"<h3 style='text-align: center;'>🎯 {home_team} vs {away_team} 승부 예측 결과</h3>", unsafe_allow_html=True)

    with st.container():
        fig = plt_OddsofWinning(home_team, away_team)
        st.pyplot(fig)

    st.markdown(f"<h4 style='text-align: center;'>🎯 {home_team} vs {away_team} 승부 예측 지표</h4>", unsafe_allow_html=True)

    
    
    with st.container():
        fig1, fig2 = plt_match_up(home_team, away_team)
        with st.container():
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                st.markdown(f"<div style='text-align: center; font-weight: bold; margin-top: 15px; margin-bottom: 20px;'>{home_team} 선발 투수 : {matches[matches['팀명1'] == home_team]['선발투수1'].values[0]}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"")
            with col3:
                st.markdown(f"<div style='text-align: center; font-weight: bold; margin-top: 15px; margin-bottom: 20px;'>{away_team} 선발 투수 : {matches[matches['팀명2'] == away_team]['선발투수2'].values[0]}</div>", unsafe_allow_html=True)


        with st.container():
            col1, col2, col3 = st.columns([2, 1, 2])  # Adjust the width ratios as needed
            with col1:
                st.pyplot(fig1)
            with col2:
                st.markdown("""
                <div style="text-align: center; font-size: 5px; width: fit-content; margin: auto;">
                    <p><strong>승률</strong></p>
                    <p><strong>팀 타율</strong></p>
                    <p><strong>선발 선수 평균자책</strong></p>
                </div>
            """, unsafe_allow_html=True)
            with col3:
                st.pyplot(fig2)

        




    