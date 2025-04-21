import streamlit as st
import sys
import pandas as pd

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../components")

from navbar import show

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
