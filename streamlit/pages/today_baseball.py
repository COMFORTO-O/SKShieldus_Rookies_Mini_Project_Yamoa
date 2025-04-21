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
            <div class="section-title">주요 뉴스</div>
        </div>
    </div>
""", unsafe_allow_html=True)
# ------------시각화 ------------
categories = get_sections()
st.markdown("## 💡 보고 싶은 뉴스 카테고리를 골라보세요!")
selected_category = None
cols = st.columns(len(categories))
for i, category in enumerate(categories):
    if cols[i].button(category):
        selected_category = category
if selected_category:
    news_list = get_news(selected_category)
    st.markdown(f"### {selected_category}")

    for news in news_list:
        st.markdown(f"#### 🔗 [{news['title']}]({news['link']})")
        if 'img' in news:
            st.image(news['img'], use_column_width=True)
else:
    news_list = get_news('최신뉴스')
    st.markdown(f"### 최신뉴스")
    
    for news in news_list:
        if 'img' in news:
            st.image(news['img'], use_column_width=True)
        st.markdown(f"#### [{news['title']}]({news['link']})")