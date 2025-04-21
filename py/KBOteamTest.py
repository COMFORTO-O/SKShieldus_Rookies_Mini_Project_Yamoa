import streamlit as st
from collections import defaultdict
import json

def get_questions():
    with open("../../csv/test_questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_teams():
    with open("../../csv/test_team.json", "r", encoding="utf-8") as f:
        return json.load(f)
# teams = [
#     {
#     "name": "SSG 랜더스",
#     "description": "감독 : 이숭용  주장 : 김광현",
#     "characteristics": "창단연도 : 2021년  연고지역 : 인천광역시",
#     "image": "../jpg/st_team_ssg.jpg"
#   },
#   {
#     "name": "키움 히어로즈",
#     "description": "감독 : 홍원기  주장 : 송성문",
#     "characteristics": "창단연도 : 2008년  연고지역 : 서울특별시",
#     "image": "../jpg/st_team_kiwoom.jpg"
#   },
#   {
#     "name": "LG 트윈스",
#     "description": "감독 : 염경엽  주장 : 박해민",
#     "characteristics": "창단연도 : 1990년  연고지역 : 서울특별시",
#     "image": "../jpg/st_team_lg.jpg"
#   },
#   {
#     "name": "KT 위즈",
#     "description": "감독 : 이강철  주장 : 장성우",
#     "characteristics": "창단연도 : 2013년  연고지역 : 수원시",
#     "image": "../jpg/st_team_kt.jpg"
#   },
#   {
#     "name": "NC 다이노스",
#     "description": "감독 : 이호준  주장 : 박민우",
#     "characteristics": "창단연도 : 2011년  연고지역 : 창원시",
#     "image": "../jpg/st_team_nc.jpg"
#   },
#   {
#     "name": "두산 베어스",
#     "description": "감독 : 이승엽  주장 : 양의지",
#     "characteristics": "창단연도 : 1982년  연고지역 : 서울특별시",
#     "image": "../jpg/doosan.jpeg"
#   },
#   {
#     "name": "KIA 타이거즈",
#     "description": "감독 : 이범호  주장 : 나성범",
#     "characteristics": "창단연도 : 2001년  연고지역 : 광주광역시",
#     "image": "../jpg/kia.jpg"
#   },
#   {
#     "name": "삼성 라이온즈",
#     "description": "감독 : 박진만  주장 : 구자욱",
#     "characteristics": "창단연도 : 1982년  연고지역 : 대구광역시",
#     "image": "../jpg/samsung.jpg"
#   },
#   {
#     "name": "롯데 자이언츠",
#     "description": "감독 : 김태형  주장 : 전준우",
#     "characteristics": "창단연도 : 1982년  연고지역 : 부산광역시",
#     "image": "../jpg/lotte.jpg"
#   },
#   {
#     "name": "한화 이글스",
#     "description": "감독 : 김경문  주장 : 채은성",
#     "characteristics": "창단연도 : 1986  연고지역 : 대전광역시",
#     "image": "../jpg/hanwha.png"
#   }
# ]



# 스타일 설정
st.markdown("""
<style>
    .question-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }
    .question-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    .choice-btn {
        width: 80%;
        max-width: 500px;
    }
    .choice-btn:hover {
        background-color: #f5f5f5; /* hover 시 배경색 */
        border-color: #72D180; /* hover 시 테두리 색 */
    }
    .choice-btn:active {
        background-color: #A5D6A7; /* 클릭 시 배경색 */
        border-color: #388E3C; /* 클릭 시 테두리 색 */
    }
    .stProgress {
        background-color: white; /* 프로그레스바 배경색 */
    }
    .stProgress > div > div  {
        background-color: #72D180; /* 프로그레스바 진행 색상 */
    }
    .progress-text {
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)



# 시작 화면
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
# 질문 렌더링 함수
def render_question(quest):
    questions = quest
    current_q = questions[st.session_state.current_question]
    
    # 진행 상태
    progress = (st.session_state.current_question + 1) / len(questions)
    st.markdown(f'<div class="progress-text">질문 {st.session_state.current_question + 1}/{len(questions)}</div>', unsafe_allow_html=True)
    st.progress(progress)
    
    # 질문 텍스트
    st.markdown(f'<div class="question-text">{current_q["question"]}</div>', unsafe_allow_html=True)
    
    # 선택지 컨테이너
    st.markdown('<div class="choice-btn">', unsafe_allow_html=True)
    
    # 선택지 버튼
    for choice in current_q["choices"]:
        if st.button(
            choice["text"],
            key=f"choice_{current_q['id']}_{choice['text']}",
            use_container_width=True,
            type="secondary"
        ):
            # 선택 처리
            for team, score in choice["scores"].items():
                st.session_state.team_scores[team] += score
            
            # 다음 질문으로 이동
            st.session_state.current_question += 1
            if st.session_state.current_question >= len(questions):
                st.session_state.submitted = True
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# 메인 로직
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
                st.image(team_info["image"], width=200)
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

            

