import streamlit as st
import pandas as pd
import json
import os
import sys

print(os.path.realpath(__file__))

# 사용자 정의 경로 추가
sys.path.append("../py")
sys.path.append("../csv")
sys.path.append("../jupyter/scraping")
sys.path.append("components")

from plt_team_rank import visualize_team_win_rate
from plt_teamrank import visualize_rank_trends, load_data_from_json
from plt_player_record import plt_player_record
from explane_navbar import show

show(1)

# 페이지 제목 및 섹션 간 여백 CSS
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
        margin: 70px 0px;        
    }
    </style>
""", unsafe_allow_html=True)






# ------------ 팀별 승수 제목 ------------ 
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">팀별 승수</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ------------ 팀별 승수 시각화 ------------ 
with st.container():
    fig = visualize_team_win_rate()  # 팀별 승수 시각화 함수 호출
    st.pyplot(fig)

    # 설명 박스
    st.markdown("""
        <div style="
            background-color: #f0f0f0;
            border-left: 5px solid #4a90e2;
            padding: 16px;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="margin-bottom: 8px;">팀별 승무패율</h4>
            <p style="margin: 0; color: #333;">
                KBO 각 팀들의 시즌별 승률, 무승부 비율, 패배율을 한눈에 확인할 수 있습니다.
                경기 수가 쌓일수록 순위와 팀의 성적 변화가 더욱 뚜렷하게 드러납니다.
            </p>
            <p style="margin: 0; color: #333;"><br>
                승리 횟수 / 경기 수, 무승부 횟수 / 경기 수, 패배 횟수 / 경기 수<br><br>
                *각 팀의 경기 수는 기상 악화, 경기장 문제 등의 이유로 다를 수 있습니다.
            </p>
        </div>
    """, unsafe_allow_html=True)











# ------------ 팀별 순위 변화 제목 ------------ 
st.markdown("""
    <div class="blank"></div>
    <div>
        <div class="section-wrapper">
            <div class="section-title">팀별 순위 변화</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------ 팀별 순위 변화 시각화 ------------ 
# JSON 파일 불러오기 → DataFrame 변환 
with st.container():
    with open("../csv/scrap_teamrank.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)

    df = load_data_from_json(json_data)
    fig = visualize_rank_trends(df)
    st.pyplot(fig)

    # 설명 박스
    st.markdown("""
        <div style="
            background-color: #f0f0f0;
            border-left: 5px solid #4a90e2;
            padding: 16px;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="margin-bottom: 8px;">팀별 순위 변화</h4>
            <p style="margin: 0; color: #333;">
                KBO 각 팀들의 순위 변화를 시각적으로 확인할 수 있어요!  
                그래프를 통해 시즌 중 어떤 팀이 상승세였고,  
                어느 팀이 주춤했는지를 한눈에 파악할 수 있습니다.  
            </p>
            <p style="margin: 0; color: #333;"><br>
                • <b>월요일</b>은 대부분 경기가 없습니다.<br>
                • 특별한 이유가 없는 한, <b>화요일~일요일</b>에 경기가 진행돼요!
            </p>
        </div>
    """, unsafe_allow_html=True)






# ------------ 선수 기록 섹션 ------------ 
st.markdown("""
    <div class="blank"></div>
    <div>
        <div class="section-wrapper">
            <div class="section-title">선수 기록</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------ 선수 기록 시각화 ------------ 
with st.container():
    # 선수 기록 시각화
    fig, fig2 = plt_player_record()  # 선수 기록 함수 호출

    st.pyplot(fig)  # 첫 번째 그래프
    # 설명 박스
    st.markdown("""
        <div style="
            background-color: #f0f0f0;
            border-left: 5px solid #4a90e2;
            padding: 16px;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
            margin-bottom: 50px;
        ">
            <h4 style="margin-bottom: 8px;">선수기록 - 타자 타율</h4>
            <p style="margin: 0; color: #333;">
                상위 15명 타자들의 타율을 확인할 수 있습니다!<br><br>
                *타율(AVG) : 안타 수 / 전체 타 수<br>
                *3할 타자라면 10번 중 3번은 안타를 친다는 의미!
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.pyplot(fig2)  # 두 번째 그래프
    # 설명 박스
    st.markdown("""
        <div style="
            background-color: #f0f0f0;
            border-left: 5px solid #4a90e2;
            padding: 16px;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="margin-bottom: 8px;">선수기록 - 투수 평균자책점</h4>
            <p style="margin: 0; color: #333;">
                상위 15명 투수들의 평균자책점을 확인할 수 있습니다!<br><br>
                *평균자책점(ERA) : 자책점 수 / 9(이닝)<br>
                *9이닝 당 투수 때문에 실점하는 점수<br>
                *수비 실책으로 인한 실점은 투수의 자책점에 포함되지 않습니다! <br>
            </p>
        </div>
    """, unsafe_allow_html=True)


    