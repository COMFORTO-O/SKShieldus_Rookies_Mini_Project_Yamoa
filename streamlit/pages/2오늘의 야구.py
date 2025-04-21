import streamlit as st
import sys, os
import pandas as pd

# 사용자 정의 경로 추가
sys.path.append("../py")
sys.path.append("../csv")
sys.path.append("../jupyter/scraping")
sys.path.append("components")

from explane_navbar import show
from weather import weather_today
from plt_OddsofWinning import plt_OddsofWinning
from ml_winrate import RF_winrate
from dataset_matchup import dataset_matchup
from scrap_match_up import scrap_match_up
from plt_match_up import plt_match_up 

show(2)

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
matches = pd.read_csv(f"../csv/scrap_match_up_main.csv", encoding='utf-8-sig')

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

# ------------ 제목 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

#------------시각화 ------------
import streamlit as st

# 야구장 이름과 코드 매핑
stadium_dict = {
    '대구야구장': '27230510',
    '마산야구장': '48160720',
    '사직야구장': '26260590',
    '목동야구장': '11470510',
    '잠실야구장': '11710720',
    '문학야구장': '28170740',
    '월명야구장': '45130680',
    '무등야구장': '29170570',
    '청주야구장': '43113630',
    '한밭야구장': '30140640'
}

st.markdown("#### 야구장 날씨 정보")  # 큰 제목
st.markdown("##### 날씨 정보를 알고 싶은 야구장을 선택해주세요.")  # 중간 제목


# 기본값 설정
if 'selected_stadium' not in st.session_state:
    st.session_state.selected_stadium = '대구야구장'

# 버튼 스타일을 작게 하기 위한 CSS 삽입
st.markdown("""
    <style>
    div.stButton > button {
        font-size: 0.7rem;
        padding: 0.25rem 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 버튼을 5개씩 나눠서 두 줄로 만들기
stadium_items = list(stadium_dict.items())

for i in range(0, len(stadium_items), 5):
    cols = st.columns(5)
    for j, (stadium_name, _) in enumerate(stadium_items[i:i+5]):
        if cols[j].button(stadium_name):
            st.session_state.selected_stadium = stadium_name

# 선택된 야구장에 대한 날씨 시각화
selected_stadium = st.session_state.selected_stadium
fig = weather_today(selected_stadium)
st.pyplot(fig)

# ------------ 제목 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title"><이건 꼭 챙기세요 !></div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
st.write('기온 28도 이상인 경우 : 손풍기, 양산, 쿨패치')
st.write('습도 60프로 이상인 경우 : 부채 !손풍기보다는 부채로!')
st.write('강수가 50프로 이상인 경우 : 우비, 우산')
#with st.container():
#    with st.container():
#        fig = visualize_team_win_rate()  # 팀별 승수 시각화 함수 호출
#        st.pyplot(fig)