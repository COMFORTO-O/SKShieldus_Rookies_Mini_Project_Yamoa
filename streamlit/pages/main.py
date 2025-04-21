import streamlit as st
import sys
import pandas as pd
import json

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../jupyter/scraping")
sys.path.append("../components")

from navbar import show
from plt_team_rank import visualize_team_win_rate
from plt_teamrank import visualize_rank_trends
from plt_player_record import plt_player_record


# Streamlit 설정을 가장 먼저 호출 - 그렇지 않으면 오류 발생생
st.set_page_config(page_title="야모아", layout="wide")

# 네비게이션 바
show()


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
    with st.container():
        fig = visualize_team_win_rate()  # 팀별 승수 시각화 함수 호출
        st.pyplot(fig)







# # ------------ 팀별 순위 변화 제목 ------------
# st.markdown("""
#     <div class="blank"></div>
#     <div>
#         <div class="section-wrapper">
#             <div class="section-title">팀별 순위 변화</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)
# # ------------ 팀별 순위 변화 시각화 ------------
# with st.container():
#     # JSON 데이터를 로드하여 DataFrame 생성
#     df = load_data_from_json(json_file_path)  # 여기서 캐시된 데이터 사용
    
#     with st.container():
#         fig_rank = visualize_rank_trends(df)  # 팀별 순위 변화 시각화 함수 호출 (df를 전달)
#         st.pyplot(fig_rank)







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
    # 팀별 승수 시각화
    fig, fig2 = plt_player_record()  # 팀별 승수 시각화 함수 호출
    st.pyplot(fig)  # 첫 번째 그래프
    st.pyplot(fig2)  # 두 번째 그래프
