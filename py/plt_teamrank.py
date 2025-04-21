import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
import os


# 한글폰트 설정 (예: 윈도우의 맑은 고딕)
font_path = 'C:\\windows\\Fonts\\malgun.ttf'
font_prop = fm.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_prop)

# JSON 파일 경로
# json_file_path = "C:/Users/user/Desktop/yamoa_project/csv/scrap_teamrank.json"


# JSON 데이터 로드
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)





# JSON 데이터를 Pandas DataFrame으로 변환
def load_data_from_json(json_data):
    all_data = []
    for team, records in json_data.items():
        for record in records:
            record["team"] = team  # 팀 이름 추가
            all_data.append(record)
    
    df = pd.DataFrame(all_data)
    
    # 날짜 형식 변환 및 내림차순 정렬 (최근 -> 과거)
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')  # 날짜 형식 변환
    df = df.sort_values(by=["date", "rank"], ascending=[False, True]).reset_index(drop=True)  # 내림차순으로 날짜 정렬
    
    return df

# 데이터 로드
df = load_data_from_json(json_data)

# 전체 팀 순위 변화를 날짜별로 시각화
# 팀별 순위 변화 시각화 함수
def visualize_rank_trends(df):
    # 팀별 순위 변화 시각화
    plt.figure(figsize=(15, 8))  # 그래프 크기 조정
    for team in df['team'].unique():
        team_data = df[df['team'] == team].sort_values(by='date', ascending=False)
        plt.plot(team_data['date'], team_data['rank'], marker='o', label=team)
    
    plt.gca().invert_yaxis()  # 순위 낮은 값이 위로 향하도록 반전
    plt.ylabel("순위", fontsize=12)
    plt.title("KBO 팀별 순위 변화", fontsize=16)
    plt.legend(title="팀", fontsize=10, loc='upper left')
    plt.yticks(range(1, 11))
    plt.grid(axis='x', linestyle='')
    plt.grid(axis='y', linestyle='-', alpha=0.7)
    
    return plt

# 그래프 시각화
visualize_rank_trends(df)
