import React, { useState } from 'react';
import { ChevronRight, RefreshCcw, Baseline as Baseball, Trophy } from 'lucide-react';

interface Question {
  id: number;
  question: string;
  choices: string[];
}

const questions: Question[] = [
  {
    id: 1,
    question: "친구와 약속이 있을 때 나는?",
    choices: [
      "정확한 시간과 장소를 미리 정한다",
      "즉흥적으로 결정해도 괜찮다",
      "친구가 정해주는 대로 따른다",
      "여러 옵션을 두고 상황에 맞게 선택한다"
    ]
  },
  {
    id: 2,
    question: "스트레스를 받았을 때 나는?",
    choices: [
      "혼자만의 시간을 가지며 충전한다",
      "친구들과 수다를 떨며 푼다",
      "격한 운동으로 해소한다",
      "맛있는 음식으로 달랜다"
    ]
  },
  {
    id: 3,
    question: "주말에 갑자기 비가 왔다. 나는?",
    choices: [
      "미리 준비한 대체 계획을 실행한다",
      "집에서 영화나 드라마를 본다",
      "우산 들고 계획대로 강행한다",
      "친구들에게 연락해서 실내 활동을 찾는다"
    ]
  },
  {
    id: 4,
    question: "새로운 취미를 시작할 때 나는?",
    choices: [
      "철저한 사전 조사부터 시작한다",
      "일단 시작하고 배워가며 발전한다",
      "관련 커뮤니티에 가입하고 정보를 얻는다",
      "경험자인 친구에게 조언을 구한다"
    ]
  },
  {
    id: 5,
    question: "여행 계획을 세울 때 나는?",
    choices: [
      "시간 단위로 세세하게 계획한다",
      "대략적인 코스만 잡아둔다",
      "유명한 코스를 따라간다",
      "현지에서 즉흥적으로 결정한다"
    ]
  },
  {
    id: 6,
    question: "좋아하는 음악을 들을 때 나는?",
    choices: [
      "가사의 의미를 깊게 생각한다",
      "멜로디와 비트에 집중한다",
      "따라 부르며 흥을 즐긴다",
      "뮤직비디오의 스토리를 분석한다"
    ]
  },
  {
    id: 7,
    question: "일이 잘 안 풀릴 때 나는?",
    choices: [
      "원인을 분석하고 해결책을 찾는다",
      "시간이 해결해줄 것이라 믿는다",
      "다른 사람의 조언을 구한다",
      "기분 전환을 위해 다른 일을 한다"
    ]
  },
  {
    id: 8,
    question: "친구가 고민을 털어놓을 때 나는?",
    choices: [
      "해결책을 제시한다",
      "공감하며 이야기를 들어준다",
      "비슷한 경험을 이야기해준다",
      "기분 전환할 수 있는 활동을 제안한다"
    ]
  },
  {
    id: 9,
    question: "새로운 환경에 적응할 때 나는?",
    choices: [
      "철저한 관찰로 분위기를 파악한다",
      "적극적으로 먼저 다가간다",
      "자연스러운 흐름을 따른다",
      "비슷한 성향의 사람을 찾는다"
    ]
  },
  {
    id: 10,
    question: "주변 사람들이 나를 표현하는 방식은?",
    choices: [
      "신중하고 계획적이다",
      "활발하고 에너지가 넘친다",
      "따뜻하고 배려심이 많다",
      "독특하고 창의적이다"
    ]
  },
  {
    id: 11,
    question: "성공한 사람을 볼 때 드는 생각은?",
    choices: [
      "어떤 노력과 과정이 있었을지 궁금하다",
      "나도 저렇게 될 수 있다고 확신한다",
      "그 사람만의 특별한 재능이 부럽다",
      "성공의 기준은 사람마다 다르다"
    ]
  },
  {
    id: 12,
    question: "휴일에 가장 선호하는 활동은?",
    choices: [
      "계획했던 일 하나씩 처리하기",
      "친구들과 신나게 놀기",
      "집에서 조용히 쉬기",
      "새로운 장소 탐방하기"
    ]
  },
  {
    id: 13,
    question: "선물을 고를 때 나는?",
    choices: [
      "실용성을 가장 중요하게 생각한다",
      "받는 사람의 취향을 고려한다",
      "특별한 의미가 담긴 것을 고른다",
      "트렌디한 아이템을 선택한다"
    ]
  },
  {
    id: 14,
    question: "단체 활동에서 나는?",
    choices: [
      "계획을 세우고 역할을 분담한다",
      "분위기를 활기차게 만든다",
      "구성원들의 의견을 조율한다",
      "아이디어를 제안한다"
    ]
  },
  {
    id: 15,
    question: "도전적인 상황에서 나는?",
    choices: [
      "철저한 준비로 위험을 최소화한다",
      "일단 부딪혀보고 배운다",
      "경험자의 조언을 참고한다",
      "직감을 믿고 결정한다"
    ]
  },
  {
    id: 16,
    question: "나의 이상적인 주말은?",
    choices: [
      "미리 계획한 일정을 차근차근 실행하기",
      "친구들과 즉흥적인 약속 잡기",
      "취미 생활에 몰두하기",
      "새로운 경험 시도하기"
    ]
  },
  {
    id: 17,
    question: "SNS를 사용할 때 나는?",
    choices: [
      "정보 수집용으로만 활용한다",
      "일상을 적극적으로 공유한다",
      "가까운 사람들과만 소통한다",
      "트렌드를 주도하려 노력한다"
    ]
  },
  {
    id: 18,
    question: "경쟁에서 이기기 위해 중요한 것은?",
    choices: [
      "체계적인 준비와 전략",
      "끝까지 포기하지 않는 열정",
      "팀워크와 협력",
      "창의적인 문제 해결"
    ]
  },
  {
    id: 19,
    question: "나의 롤모델은?",
    choices: [
      "뚜렷한 목표를 향해 나아가는 사람",
      "끊임없이 도전하는 사람",
      "타인을 배려하고 이끄는 사람",
      "자신만의 색깔을 가진 사람"
    ]
  },
  {
    id: 20,
    question: "10년 후의 나는?",
    choices: [
      "안정적이고 계획적인 삶을 살고 있다",
      "끊임없이 새로운 도전을 하고 있다",
      "주변 사람들과 조화롭게 지낸다",
      "나만의 특별한 가치를 만들어간다"
    ]
  }
];

const teams = [
  {
    name: "SSG 랜더스",
    description: "혁신적이고 과학적인 야구를 추구하는 인천의 자부심",
    characteristics: "데이터 기반의 전략적 경기 운영, 젊은 선수 육성",
    image: "https://images.unsplash.com/photo-1562077772-3bd90403f7f0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "키움 히어로즈",
    description: "젊고 역동적인 에너지가 넘치는 서울의 새로운 강자",
    characteristics: "공격적인 야구, 신생팀의 패기",
    image: "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "LG 트윈스",
    description: "전통과 실력을 겸비한 서울의 자존심",
    characteristics: "안정적인 팀 운영, 탄탄한 기본기",
    image: "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "KT 위즈",
    description: "빠르게 성장하는 수원의 젊은 팀",
    characteristics: "스마트한 경기 운영, 체계적인 선수 육성",
    image: "https://images.unsplash.com/photo-1471295253337-3ceaaad65897?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "NC 다이노스",
    description: "창의적이고 혁신적인 창원의 공룡군단",
    characteristics: "데이터 기반 야구, 장기적 비전",
    image: "https://images.unsplash.com/photo-1508163223045-1880bc36e222?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "두산 베어스",
    description: "강한 전통과 저력을 가진 서울의 명문",
    characteristics: "안정적인 선수층, 탄탄한 프런트",
    image: "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "KIA 타이거즈",
    description: "열정적인 팬덤을 가진 광주의 호랑이군단",
    characteristics: "뜨거운 응원 문화, 지역 밀착형 운영",
    image: "https://images.unsplash.com/photo-1562077772-3bd90403f7f0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "삼성 라이온즈",
    description: "왕조의 자존심을 가진 대구의 사자군단",
    characteristics: "체계적인 선수 육성, 강한 승부 근성",
    image: "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "롯데 자이언츠",
    description: "뜨거운 야구 도시 부산의 자부심",
    characteristics: "열정적인 팬 문화, 화끈한 공격 야구",
    image: "https://images.unsplash.com/photo-1508163223045-1880bc36e222?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "한화 이글스",
    description: "불굴의 의지를 가진 대전의 독수리군단",
    characteristics: "끈기 있는 재건, 젊은 선수 육성",
    image: "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
  }
];

function App() {
  const [isStarted, setIsStarted] = useState(false);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<number[]>([]);
  const [showResult, setShowResult] = useState(false);
  const [matchedTeam, setMatchedTeam] = useState<typeof teams[0] | null>(null);

  const handleStart = () => {
    setIsStarted(true);
  };

  const calculateResult = () => {
    const traits = {
      analytical: 0,
      passionate: 0,
      traditional: 0,
      innovative: 0,
    };

    answers.forEach((answer) => {
      switch (answer) {
        case 0:
          traits.analytical += 1;
          break;
        case 1:
          traits.passionate += 1;
          break;
        case 2:
          traits.traditional += 1;
          break;
        case 3:
          traits.innovative += 1;
          break;
      }
    });

    const maxTrait = Object.entries(traits).reduce((a, b) => 
      traits[a[0] as keyof typeof traits] > traits[b[0] as keyof typeof traits] ? a : b
    )[0];

    let matchedTeam;
    switch (maxTrait) {
      case 'analytical':
        matchedTeam = teams[Math.floor(Math.random() * 2)];
        break;
      case 'passionate':
        matchedTeam = teams[Math.floor(Math.random() * 2) + 6];
        break;
      case 'traditional':
        matchedTeam = teams[Math.floor(Math.random() * 2) + 2];
        break;
      case 'innovative':
        matchedTeam = teams[Math.floor(Math.random() * 2) + 4];
        break;
      default:
        matchedTeam = teams[Math.floor(Math.random() * teams.length)];
    }

    setMatchedTeam(matchedTeam);
  };

  const handleAnswer = (choiceIndex: number) => {
    const newAnswers = [...answers, choiceIndex];
    setAnswers(newAnswers);

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      setShowResult(true);
      calculateResult();
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setAnswers([]);
    setShowResult(false);
    setMatchedTeam(null);
    setIsStarted(false);
  };

  if (!isStarted) {
    return (
      <div className="min-h-screen bg-[url('https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80')] bg-cover bg-center bg-no-repeat">
        <div className="min-h-screen bg-gradient-to-b from-green-950/90 to-green-900/90 flex items-center justify-center p-4">
          <div className="bg-white/95 backdrop-blur-sm rounded-lg shadow-2xl p-8 max-w-lg w-full text-center border-t-4 border-green-700">
            <div className="flex justify-center mb-4">
              <Baseball size={56} className="text-green-700" strokeWidth={1.5} />
            </div>
            <h1 className="text-4xl font-black text-green-950 mb-2 font-kbo">야모아</h1>
            <h2 className="text-xl text-green-800 mb-6 font-kbo">내가 좋아하게 될 팀은?</h2>
            <p className="text-gray-600 mb-8">
              20가지 질문으로 알아보는 나의 최애 야구팀 찾기
            </p>
            <button
              onClick={handleStart}
              className="w-full bg-green-700 text-white py-4 rounded-lg hover:bg-green-800 transition-colors flex items-center justify-center gap-2 text-lg font-semibold shadow-lg font-kbo"
            >
              테스트 시작하기
              <ChevronRight size={20} />
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (showResult && matchedTeam) {
    return (
      <div className="min-h-screen bg-[url('https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80')] bg-cover bg-center bg-no-repeat">
        <div className="min-h-screen bg-gradient-to-b from-green-950/90 to-green-900/90 flex items-center justify-center p-4">
          <div className="bg-white/95 backdrop-blur-sm rounded-lg shadow-2xl p-8 max-w-lg w-full border-t-4 border-green-700">
            <div className="flex justify-center mb-6">
              <Trophy size={56} className="text-green-700" strokeWidth={1.5} />
            </div>
            <h2 className="text-2xl font-bold text-center mb-6 text-green-900 font-kbo">
              당신과 가장 잘 맞는 구단은...
            </h2>
            <div className="mb-8">
              <div className="relative w-full h-48 mb-4 rounded-lg overflow-hidden shadow-lg">
                <img
                  src={matchedTeam.image}
                  alt={matchedTeam.name}
                  className="absolute inset-0 w-full h-full object-cover transform hover:scale-105 transition-transform duration-300"
                />
                <div className="absolute inset-0 bg-black/20 hover:bg-black/10 transition-colors"></div>
              </div>
              <h3 className="text-2xl font-bold text-center mb-2 text-green-800 font-kbo">{matchedTeam.name}</h3>
              <p className="text-gray-700 text-center mb-4">{matchedTeam.description}</p>
              <p className="text-sm text-gray-600 text-center">{matchedTeam.characteristics}</p>
            </div>
            <button
              onClick={resetQuiz}
              className="w-full bg-green-700 text-white py-3 rounded-lg hover:bg-green-800 transition-colors flex items-center justify-center gap-2 shadow-lg font-kbo"
            >
              <RefreshCcw size={20} />
              다시 테스트하기
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[url('https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80')] bg-cover bg-center bg-no-repeat">
      <div className="min-h-screen bg-gradient-to-b from-green-950/90 to-green-900/90 flex items-center justify-center p-4">
        <div className="bg-white/95 backdrop-blur-sm rounded-lg shadow-2xl p-8 max-w-lg w-full border-t-4 border-green-700">
          <div className="mb-8">
            <div className="flex justify-between items-center mb-4">
              <span className="text-sm text-gray-600 font-semibold font-kbo">
                {currentQuestion + 1} / {questions.length}
              </span>
              <div className="h-2 flex-1 mx-4 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-green-600 transition-all duration-300"
                  style={{
                    width: `${((currentQuestion + 1) / questions.length) * 100}%`,
                  }}
                />
              </div>
            </div>
            <h2 className="text-xl font-bold text-green-900 font-kbo">
              {questions[currentQuestion].question}
            </h2>
          </div>
          <div className="space-y-3">
            {questions[currentQuestion].choices.map((choice, index) => (
              <button
                key={index}
                onClick={() => handleAnswer(index)}
                className="w-full text-left p-4 rounded-lg border border-gray-200 hover:border-green-500 hover:bg-green-50 transition-colors flex items-center justify-between group shadow-sm font-kbo"
              >
                <span className="text-gray-700 group-hover:text-green-700">{choice}</span>
                <ChevronRight
                  size={20}
                  className="text-gray-400 group-hover:text-green-500"
                />
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

