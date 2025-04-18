import streamlit as st
from collections import defaultdict
import json


# 질문 목록
questions = [
    {
        "id": 1,
        "question": "친구와 약속이 있을 때 나는?",
        "choices": [
            {"text": "정확한 시간과 장소를 미리 정한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "즉흥적으로 결정해도 괜찮다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "친구가 정해주는 대로 따른다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "여러 옵션을 두고 상황에 맞게 선택한다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "SSG 랜더스": 1}}
        ]
    },
    {
        "id": 2,
        "question": "스트레스를 받았을 때 나는?",
        "choices": [
            {"text": "혼자만의 시간을 가지며 충전한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "한화 이글스": 1}},
            {"text": "친구들과 수다를 떨며 푼다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "KIA 타이거즈": 1}},
            {"text": "격한 운동으로 해소한다", "scores": {"두산 베어스": 2, "삼성 라이온즈": 1, "KT 위즈": 1}},
            {"text": "맛있는 음식으로 달랜다", "scores": {"NC 다이노스": 2, "롯데 자이언츠": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 3,
        "question": "주말에 갑자기 비가 왔다. 나는?",
        "choices": [
            {"text": "미리 준비한 대체 계획을 실행한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "집에서 영화나 드라마를 본다", "scores": {"한화 이글스": 2, "삼성 라이온즈": 1, "두산 베어스": 1}},
            {"text": "우산 들고 계획대로 강행한다", "scores": {"두산 베어스": 2, "KIA 타이거즈": 1, "롯데 자이언츠": 1}},
            {"text": "친구들에게 연락해서 실내 활동을 찾는다", "scores": {"키움 히어로즈": 2, "NC 다이노스": 1, "KT 위즈": 1}}
        ]
    },
    {
        "id": 4,
        "question": "새로운 취미를 시작할 때 나는?",
        "choices": [
            {"text": "철저한 사전 조사부터 시작한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "일단 시작하고 배워가며 발전한다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "관련 커뮤니티에 가입하고 정보를 얻는다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "삼성 라이온즈": 1}},
            {"text": "경험자인 친구에게 조언을 구한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}}
        ]
    },
    {
        "id": 5,
        "question": "여행 계획을 세울 때 나는?",
        "choices": [
            {"text": "시간 단위로 세세하게 계획한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "대략적인 코스만 잡아둔다", "scores": {"NC 다이노스": 2, "키움 히어로즈": 1, "롯데 자이언츠": 1}},
            {"text": "유명한 코스를 따라간다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "현지에서 즉흥적으로 결정한다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}}
        ]
    },
    {
        "id": 6,
        "question": "좋아하는 음악을 들을 때 나는?",
        "choices": [
            {"text": "가사의 의미를 깊게 생각한다", "scores": {"LG 트윈스": 2, "SSG 랜더스": 1, "KT 위즈": 1}},
            {"text": "멜로디와 비트에 집중한다", "scores": {"롯데 자이언츠": 2, "키움 히어로즈": 1, "NC 다이노스": 1}},
            {"text": "따라 부르며 흥을 즐긴다", "scores": {"KIA 타이거즈": 2, "삼성 라이온즈": 1, "두산 베어스": 1}},
            {"text": "뮤직비디오의 스토리를 분석한다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 7,
        "question": "일이 잘 안 풀릴 때 나는?",
        "choices": [
            {"text": "원인을 분석하고 해결책을 찾는다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "시간이 해결해줄 것이라 믿는다", "scores": {"한화 이글스": 2, "롯데 자이언츠": 1, "삼성 라이온즈": 1}},
            {"text": "다른 사람의 조언을 구한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "기분 전환을 위해 다른 일을 한다", "scores": {"키움 히어로즈": 2, "NC 다이노스": 1, "KT 위즈": 1}}
        ]
    },
    {
        "id": 8,
        "question": "친구가 고민을 털어놓을 때 나는?",
        "choices": [
            {"text": "해결책을 제시한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "공감하며 이야기를 들어준다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "비슷한 경험을 이야기해준다", "scores": {"NC 다이노스": 2, "롯데 자이언츠": 1, "한화 이글스": 1}},
            {"text": "기분 전환할 수 있는 활동을 제안한다", "scores": {"키움 히어로즈": 2, "KT 위즈": 1, "NC 다이노스": 1}}
        ]
    },
    {
        "id": 9,
        "question": "새로운 환경에 적응할 때 나는?",
        "choices": [
            {"text": "철저한 관찰로 분위기를 파악한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "적극적으로 먼저 다가간다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "자연스러운 흐름을 따른다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "비슷한 성향의 사람을 찾는다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 10,
        "question": "주변 사람들이 나를 표현하는 방식은?",
        "choices": [
            {"text": "신중하고 계획적이다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "활발하고 에너지가 넘친다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "따뜻하고 배려심이 많다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "독특하고 창의적이다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 11,
        "question": "성공한 사람을 볼 때 드는 생각은?",
        "choices": [
            {"text": "어떤 노력과 과정이 있었을지 궁금하다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "나도 저렇게 될 수 있다고 확신한다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "그 사람만의 특별한 재능이 부럽다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "성공의 기준은 사람마다 다르다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 12,
        "question": "휴일에 가장 선호하는 활동은?",
        "choices": [
            {"text": "계획했던 일 하나씩 처리하기", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "친구들과 신나게 놀기", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "집에서 조용히 쉬기", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "새로운 장소 탐방하기", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 13,
        "question": "선물을 고를 때 나는?",
        "choices": [
            {"text": "실용성을 가장 중요하게 생각한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "받는 사람의 취향을 고려한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "특별한 의미가 담긴 것을 고른다", "scores": {"NC 다이노스": 2, "롯데 자이언츠": 1, "한화 이글스": 1}},
            {"text": "트렌디한 아이템을 선택한다", "scores": {"키움 히어로즈": 2, "KT 위즈": 1, "NC 다이노스": 1}}
        ]
    },
    {
        "id": 14,
        "question": "단체 활동에서 나는?",
        "choices": [
            {"text": "계획을 세우고 역할을 분담한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "분위기를 활기차게 만든다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "구성원들의 의견을 조율한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "아이디어를 제안한다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 15,
        "question": "도전적인 상황에서 나는?",
        "choices": [
            {"text": "철저한 준비로 위험을 최소화한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "일단 부딪혀보고 배운다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "경험자의 조언을 참고한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "직감을 믿고 결정한다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 16,
        "question": "나의 이상적인 주말은?",
        "choices": [
            {"text": "미리 계획한 일정을 차근차근 실행하기", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "친구들과 즉흥적인 약속 잡기", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "취미 생활에 몰두하기", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "새로운 경험 시도하기", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 17,
        "question": "SNS를 사용할 때 나는?",
        "choices": [
            {"text": "정보 수집용으로만 활용한다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "일상을 적극적으로 공유한다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "가까운 사람들과만 소통한다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "트렌드를 주도하려 노력한다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 18,
        "question": "경쟁에서 이기기 위해 중요한 것은?",
        "choices": [
            {"text": "체계적인 준비와 전략", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "끝까지 포기하지 않는 열정", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "팀워크와 협력", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "창의적인 문제 해결", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 19,
        "question": "나의 롤모델은?",
        "choices": [
            {"text": "뚜렷한 목표를 향해 나아가는 사람", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "끊임없이 도전하는 사람", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "타인을 배려하고 이끄는 사람", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "자신만의 색깔을 가진 사람", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    },
    {
        "id": 20,
        "question": "10년 후의 나는?",
        "choices": [
            {"text": "안정적이고 계획적인 삶을 살고 있다", "scores": {"SSG 랜더스": 2, "LG 트윈스": 1, "KT 위즈": 1}},
            {"text": "끊임없이 새로운 도전을 하고 있다", "scores": {"키움 히어로즈": 2, "롯데 자이언츠": 1, "NC 다이노스": 1}},
            {"text": "주변 사람들과 조화롭게 지낸다", "scores": {"삼성 라이온즈": 2, "KIA 타이거즈": 1, "두산 베어스": 1}},
            {"text": "나만의 특별한 가치를 만들어간다", "scores": {"NC 다이노스": 2, "KT 위즈": 1, "한화 이글스": 1}}
        ]
    }
]

teams = [
    {
    "name": "SSG 랜더스",
    "description": "혁신적이고 과학적인 야구를 추구하는 인천의 자부심",
    "characteristics": "데이터 기반의 전략적 경기 운영, 젊은 선수 육성",
    "image": "https://images.unsplash.com/photo-1562077772-3bd90403f7f0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "키움 히어로즈",
    "description": "젊고 역동적인 에너지가 넘치는 서울의 새로운 강자",
    "characteristics": "공격적인 야구, 신생팀의 패기",
    "image": "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "LG 트윈스",
    "description": "전통과 실력을 겸비한 서울의 자존심",
    "characteristics": "안정적인 팀 운영, 탄탄한 기본기",
    "image": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "KT 위즈",
    "description": "빠르게 성장하는 수원의 젊은 팀",
    "characteristics": "스마트한 경기 운영, 체계적인 선수 육성",
    "image": "https://images.unsplash.com/photo-1471295253337-3ceaaad65897?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "NC 다이노스",
    "description": "창의적이고 혁신적인 창원의 공룡군단",
    "characteristics": "데이터 기반 야구, 장기적 비전",
    "image": "https://images.unsplash.com/photo-1508163223045-1880bc36e222?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "두산 베어스",
    "description": "강한 전통과 저력을 가진 서울의 명문",
    "characteristics": "안정적인 선수층, 탄탄한 프런트",
    "image": "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "KIA 타이거즈",
    "description": "열정적인 팬덤을 가진 광주의 호랑이군단",
    "characteristics": "뜨거운 응원 문화, 지역 밀착형 운영",
    "image": "https://images.unsplash.com/photo-1562077772-3bd90403f7f0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "삼성 라이온즈",
    "description": "왕조의 자존심을 가진 대구의 사자군단",
    "characteristics": "체계적인 선수 육성, 강한 승부 근성",
    "image": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "롯데 자이언츠",
    "description": "뜨거운 야구 도시 부산의 자부심",
    "characteristics": "열정적인 팬 문화, 화끈한 공격 야구",
    "image": "https://images.unsplash.com/photo-1508163223045-1880bc36e222?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    "name": "한화 이글스",
    "description": "불굴의 의지를 가진 대전의 독수리군단",
    "characteristics": "끈기 있는 재건, 젊은 선수 육성",
    "image": "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  }
]


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
    .choice-container {
        width: 80%;
        max-width: 500px;
    }
    .choice-btn {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        background-color: white;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 16px;
    }
    .choice-btn:hover {
        background-color: #f5f5f5;
        border-color: #72D180;
    }
    .stProgress > div > div > div {
        background-color: #72D180; /* 프로그레스바 색상 변경 */
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

# 질문 렌더링 함수
def render_question():
    current_q = questions[st.session_state.current_question]
    
    # 진행 상태
    progress = (st.session_state.current_question + 1) / len(questions)
    st.markdown(f'<div class="progress-text">질문 {st.session_state.current_question + 1}/{len(questions)}</div>', unsafe_allow_html=True)
    st.progress(progress)
    
    # 질문 텍스트
    st.markdown(f'<div class="question-text">{current_q["question"]}</div>', unsafe_allow_html=True)
    
    # 선택지 컨테이너
    st.markdown('<div class="choice-container">', unsafe_allow_html=True)
    
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
        render_question()
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
        .stImage img {
            display: block; /* 이미지 블록 요소로 설정 */
            margin-left: auto; /* 왼쪽 여백 자동 */
            margin-right: auto; /* 오른쪽 여백 자동 */
            width: 50%; /* 이미지 크기를 반으로 줄임 */
        }
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
                st.image(team_info["image"], use_column_width=True)
                st.markdown(f'<div class="team-name">{team_info["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="team-description">{team_info["description"]}</div>', unsafe_allow_html=True)
                # Save the best team(s) to a file for use in another script
                with open("best_team.json", "w", encoding="utf-8") as f:
                    json.dump({"best_teams": best_teams}, f, ensure_ascii=False, indent=4)
                st.write(f"Best Teams: {best_teams}")
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

            

