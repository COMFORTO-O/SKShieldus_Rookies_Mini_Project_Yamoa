import streamlit as st
from PIL import Image



logo = Image.open("../assets/로고 배경 있음1.jpg")
st.image(logo, use_column_width=True)

# 스타일 적용
st.markdown("""
    <style>
        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 10px;
            color: #1f2937;
        }
        .section-subtitle {
            font-size: 18px;
            color: #333;
            margin-bottom: 20px;
        }
        .section-content {
            font-size: 16px;
            line-height: 1.6;
            color: #333;
            padding-left: 10px;
        }
        hr {
            border: 0;
            height: 1px;
            background: #e0e0e0;
            margin: 40px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 홈
st.markdown("""
    <div class="section-title">메인</div>
    <div class="section-content">
        야구 팬들을 위한 다양한 데이터를 한곳에서 확인할 수 있는 페이지입니다.  
        각종 야구 기록들을 직관적으로 확인할 수 있도록 그래프 형태로 제공하여 데이터를 쉽게 이해할 수 있도록 도와줍니다.  
        팀별 기록, 선수별 기록, 최근 순위 흐름 등을 한눈에 볼 수 있어, 야구 경기를 더 깊이 즐기고 싶은 분들께 유용합니다.
    </div>
    <hr>
""", unsafe_allow_html=True)

# 오늘의 야구
st.markdown("""
    <div class="section-title">오늘의 야구</div>
    <div class="section-content">
        오늘 하루 열릴 야구 경기와 관련된 다양한 정보들을 한눈에 확인할 수 있는 페이지입니다.  
        <br><br>
        • <strong>오늘의 경기 정보</strong> : 각 팀의 경기 일정부터 선수 라인업, 팀 전략의 주요 포인트를 확인할 수 있습니다.  
        <br>
        • <strong>승부 예측 및 팀 기록</strong> : 현재 시즌 데이터와 머신러닝 분석을 기반으로 승패를 예측하는 기능도 제공합니다.  
        <br>
        • <strong>날씨 정보</strong> : 경기 장소의 구장 날씨 및 환경 조건도 함께 제공되어, 경기 관람 준비에 도움이 됩니다.  
        <br><br>
        야구와 관련된 최신 정보를 실시간으로 얻고 싶다면, 이 페이지가 최고의 도우미가 될 거예요.
    </div>
    <hr>
""", unsafe_allow_html=True)

# 입덕 가이드
st.markdown("""
    <div class="section-title">입덕가이드</div>
    <div class="section-content">
        야구가 생소하거나 이제 막 관심을 가지기 시작한 분들을 위한 맞춤형 콘텐츠를 제공합니다.  
        야구를 더 재밌게 즐길 수 있도록 다양한 도구와 정보들을 준비했어요.
        <br><br>
        • <strong>유형 테스트</strong> : 당신의 취향과 성향을 바탕으로 어울리는 팀을 추천해주는 재미있는 테스트!  
        <br>
        • <strong>야구 뉴스</strong> : 최신 야구 관련 소식, 경기 리뷰, 선수 인터뷰까지 한눈에 확인할 수 있어요.
        <br>
        • <strong>구단 정보</strong> : KBO 리그에 속한 각 구단들의 상세한 소개와 특징을 확인할 수 있으며, 각 구단의 히스토리와 주요 선수 정보도 제공됩니다.  
        <br><br>
        입덕가이드는 새로운 팬들이 야구에 빠져드는 시작점이자, 기존 팬들에게는 재발견의 기회를 제공합니다.
  
    </div>
""", unsafe_allow_html=True)
