import streamlit as st
import sys
import pandas as pd
import sys
import os

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../components")

from weather import weather_today
from navbar import show
from scrap_news import get_news, get_sections

# 네브바 보이기
show()

weather_today()

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

# ------------ 제목 ------------
st.markdown("""
    <div>
        <div class="section-wrapper">
            <div class="section-title">주요 뉴스</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
#with st.container():
#    with st.container():
#        fig = visualize_team_win_rate()  # 팀별 승수 시각화 함수 호출
#        st.pyplot(fig)
