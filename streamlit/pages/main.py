import streamlit as st
import sys
import pandas as pd
import json

# Streamlit 설정을 가장 먼저 호출
st.set_page_config(page_title="야모아", layout="wide")

# 사용자 정의 경로 추가
sys.path.append("../../py")
sys.path.append("../components")
from navbar import show
from plt_team_rank import visualize_team_win_rate
from plt_teamrank import visualize_rank_trends
from plt_player_record import plt_player_record

# JSON 파일 경로
json_file_path = r"C:\Users\user\Desktop\yamoa_project\csv\scrap_teamrank.json"

# JSON 파일 로드 함수
@st.cache
def load_data_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    # JSON 데이터를 DataFrame으로 변환
    all_data = []
    for team, records in json_data.items():
        for record in records:
            record["team"] = team  # 팀 이름 추가
            all_data.append(record)
    
    # DataFrame 생성
    df = pd.DataFrame(all_data)
    
    # 날짜 변환 및 내림차순 정렬 (최근 -> 과거)
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')  # 날짜 형식 변환
    df = df.sort_values(by=["date", "rank"], ascending=[False, True]).reset_index(drop=True)  # 내림차순으로 날짜 정렬
    
    return df

# 네비게이션 바
show()

# 페이지 제목 및 섹션 구분
st.markdown("""
    <style>
    .block-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
    }
    .block {
        margin: 10px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 8px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        width: 48%;
        min-width: 300px;
        background-color: #f9f9f9;
        font-weight: bold;
    }
    </style>
    
    <div>
        <div class="block">팀별 승수</div>
    </div>
""", unsafe_allow_html=True)

# 팀별 승수 시각화
with st.container():
    with st.container():
        fig = visualize_team_win_rate()  # 팀별 승수 시각화 함수 호출
        st.pyplot(fig)

# 팀별 순위 변화 섹션
st.markdown("""
    <div>
        <div class="block">팀별 순위 변화</div>
    </div>
""", unsafe_allow_html=True)

# 팀별 순위 변화 시각화
with st.container():
    # JSON 데이터를 로드하여 DataFrame 생성
    df = load_data_from_json(json_file_path)  # 여기서 캐시된 데이터 사용
    
    with st.container():
        fig_rank = visualize_rank_trends(df)  # 팀별 순위 변화 시각화 함수 호출 (df를 전달)
        st.pyplot(fig_rank)


# 선수 기록 섹션
st.markdown("""
    <div>
        <div class="block">선수 기록</div>
    </div>
""", unsafe_allow_html=True)

# 선수 기록 시각화
with st.container():
    # 팀별 승수 시각화
    fig, fig2 = plt_player_record()  # 팀별 승수 시각화 함수 호출
    st.pyplot(fig)  # 첫 번째 그래프
    st.pyplot(fig2)  # 두 번째 그래프
