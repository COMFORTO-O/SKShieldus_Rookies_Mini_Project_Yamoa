import streamlit as st

st.set_page_config(page_title="어울리는 KBO 팀 테스트", page_icon="⚾")

# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state.page = "start"
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "scores" not in st.session_state:
    st.session_state.scores = {
        "롯데": 0, "LG": 0, "두산": 0, "한화": 0, "SSG": 0,
        "기아": 0, "삼성": 0, "NC": 0, "KT": 0, "키움": 0
    }

# 질문 데이터
questions = [
    {
        "question": "나는 응원할 때 시끄럽고 열정적인 걸 좋아한다.",
        "yes": ["롯데", "기아", "SSG"],
        "no": ["한화", "LG"]
    },
    {
        "question": "나는 최근 우승을 노릴 수 있는 강팀을 좋아한다.",
        "yes": ["LG", "KT", "SSG"],
        "no": ["한화", "롯데"]
    },
    {
        "question": "나는 팀의 역사와 전통을 중요하게 생각한다.",
        "yes": ["두산", "삼성", "롯데"],
        "no": ["NC", "KT"]
    },
    {
        "question": "나는 조용히 경기를 관람하는 걸 좋아한다.",
        "yes": ["한화", "LG", "삼성"],
        "no": ["SSG", "기아"]
    },
    {
        "question": "나는 지역 연고 의식을 중요하게 생각한다.",
        "yes": ["기아", "NC", "삼성", "한화"],
        "no": ["키움", "KT"]
    }
]

# 팀 설명
team_descriptions = {
    "롯데": "열정 넘치는 부산의 야구! 롯데 자이언츠!",
    "LG": "꾸준하고 조용한 강호, LG 트윈스!",
    "두산": "전통과 경험의 강팀, 두산 베어스!",
    "한화": "충청도의 인내와 기다림, 한화 이글스!",
    "SSG": "새롭고 강한 명문 팀, SSG 랜더스!",
    "기아": "열혈 호랑이 군단, KIA 타이거즈!",
    "삼성": "대구를 대표하는 클래식 명문, 삼성 라이온즈!",
    "NC": "창원의 젊은 힘, NC 다이노스!",
    "KT": "신흥 강호, 수원의 KT 위즈!",
    "키움": "서울의 민첩한 팀, 키움 히어로즈!"
}

# 시작 페이지
def show_start():
    st.title("⚾ 나에게 어울리는 KBO 팀은?")
    st.write("성향에 따라 어떤 야구팀의 팬이 잘 어울릴지 알아보는 간단한 테스트입니다!")
    if st.button("테스트 시작하기"):
        st.session_state.page = "question"
        st.session_state.question_index = 0
        st.session_state.scores = {team: 0 for team in st.session_state.scores}

# 질문 하나씩 보여주는 페이지
def show_question():
    index = st.session_state.question_index
    if index < len(questions):
        q = questions[index]
        st.title("질문")
        st.write(f"{index+1}. {q['question']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("예"):
                for team in q["yes"]:
                    st.session_state.scores[team] += 1
                st.session_state.question_index += 1
                st.experimental_rerun()

        with col2:
            if st.button("아니오"):
                for team in q["no"]:
                    st.session_state.scores[team] += 1
                st.session_state.question_index += 1
                st.experimental_rerun()
    else:
        st.session_state.page = "result"
        st.experimental_rerun()

# 결과 페이지
def show_result():
    best_team = max(st.session_state.scores, key=st.session_state.scores.get)
    st.title("📣 테스트 결과")
    st.subheader(f"당신에게 어울리는 팀은: **{best_team}**!")
    st.write(team_descriptions.get(best_team, "설명이 준비되지 않았어요."))
    st.image(f"https://sports-phinf.pstatic.net/team/kbo/logo/{best_team}.png", width=200)

    if st.button("다시 테스트하기"):
        st.session_state.page = "start"
        st.session_state.question_index = 0
        st.session_state.scores = {team: 0 for team in st.session_state.scores}
        st.experimental_rerun()

# 페이지 라우팅
if st.session_state.page == "start":
    show_start()
elif st.session_state.page == "question":
    show_question()
elif st.session_state.page == "result":
    show_result()
