import streamlit as st
import sys
import pandas as pd
import sys
import json
from collections import defaultdict

# 사용자 정의 경로 추가
sys.path.append("../py")
sys.path.append("../components")
sys.path.append("../csv")
sys.path.append("components")

from explane_navbar import show
from scrap_news import get_news, get_sections
from scrap_team_info import scrap_team_info
from KBOteamTest import render_question, get_questions, get_teams


show(3)

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

# ------------ 테스트 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">야구 심리테스트</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
if 'current_question' not in st.session_state:
    st.markdown("""
    <style>
    .title {
        font-size: 25px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 35px;
        text-align: center;
        margin-bottom: 20px;
    }
    .subsubtitle {
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">⚾ 야모아</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">나에게 어울리는 KBO 팀은?</h2>', unsafe_allow_html=True)
    st.markdown('<h2 class="subsubtitle">20가지 질문으로 알아보는 나의 최애 야구팀 찾기</h2>', unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("테스트 시작하기", type="primary", use_container_width=True):
            st.session_state.current_question = 0
            st.session_state.team_scores = defaultdict(int)
            st.session_state.submitted = False
            st.rerun()
    st.markdown("---")
    st.stop()
    
questions = get_questions()
teams = get_teams()
if not st.session_state.submitted:
    if st.session_state.current_question < len(questions):
        render_question(questions)
    else:
        st.session_state.submitted = True
        st.rerun()
else:
    # 결과 화면
    if st.session_state.team_scores:
        max_score = max(st.session_state.team_scores.values())
        best_teams = [team for team, score in st.session_state.team_scores.items() if score == max_score]
        
        st.markdown("""
        <style>
        
        .result-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        .result-title {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .team-name {
            font-size: 24px;
            font-weight: bold;
            margin-top: 10px;
            text-align: center;
        }
        .team-description {
            font-size: 18px;
            text-align: center;
            margin-top: 10px;
        }
        .retry-btn {
            margin-top: 20px;
        }
        
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.markdown('<div class="result-title">당신과 가장 잘 맞는 구단은...</div>', unsafe_allow_html=True)
        
        for team_name in best_teams:
            team_info = next((team for team in teams if team["name"] == team_name), None)
            if team_info:
                st.image(team_info["image"])
                st.markdown(f'<div class="team-name">{team_info["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="team-description">{team_info["description"]}</div>', unsafe_allow_html=True)
                # Save the best team(s) to a file for use in another script
                with open("best_team.json", "w", encoding="utf-8") as f:
                    json.dump({"best_teams": best_teams}, f, ensure_ascii=False, indent=4)
        st.markdown('</div>', unsafe_allow_html=True)
       

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("테스트 다시하기", key="retry_start", use_container_width=True):
                st.session_state.clear()
                st.session_state.current_question = 0
                st.session_state.team_scores = defaultdict(int)
                st.session_state.submitted = False
                st.rerun()
                
                
    else:
        st.warning("답변이 없습니다. 테스트를 다시 시작해주세요.")
        if st.button("테스트 다시하기", key="retry_start", use_container_width=True):
            st.session_state.clear()
            st.session_state.current_question = 0
            st.session_state.team_scores = defaultdict(int)
            st.session_state.submitted = False
            st.rerun()
            # Save the best team(s) to a file for use in another script
            with open("best_team.json", "w", encoding="utf-8") as f:
                json.dump({"best_teams": best_teams}, f, ensure_ascii=False, indent=4)
    
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