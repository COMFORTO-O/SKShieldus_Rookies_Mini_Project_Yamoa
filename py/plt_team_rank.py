import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import sys, os

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, '..', 'csv', 'scrap_team_rank.csv')



def visualize_team_win_rate():
    font_path = 'C:\\windows\\Fonts\\malgun.ttf'
    font_prop = fm.FontProperties(fname=font_path).get_name()
    
    # rc(run command)
    matplotlib.rc('font', family=font_prop)
    
    df_team = pd.read_csv(csv_path)

    # 승률 기준으로 오름차순 정렬
    df_team = df_team.sort_values(by='승률', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 7))  # 새로운 figure와 ax 객체 생성

    y = range(len(df_team))  # y축은 팀명 인덱스

    # 승률, 무승부율, 패배율
    draw_rate = 1 - df_team['승률'] - df_team['패배율']
    df_team['무승부율'] = draw_rate

    ax.barh(y, df_team['승률'], label='승률', color='pink')  # 가로 막대 그래프
    ax.barh(y, df_team['무승부율'], left=df_team['승률'], label='무승부율', color='lightgray')  # 왼쪽에 무승부율
    ax.barh(y, df_team['패배율'], left=df_team['승률'] + df_team['무승부율'], label='패배율', color='skyblue')  # 패배율은 나머지

    ax.set_yticks(y)  # y축은 팀명
    ax.set_yticklabels(df_team['팀명'])

    # 값 표시
    for i, rate in enumerate(df_team['승률']):
        total = df_team.loc[i, ['승률', '무승부율', '패배율']].sum()
        ax.text(total - 0.53, i, f'{rate:.3f}%', ha='center', fontsize=10, color='black')

    # plot 특징 수정
    ax.legend(loc='upper right')
    ax.set_xlim(0, 1.0)  # x축의 범위를 0부터 1까지 설정
    ax.set_ylabel('팀명')
    ax.set_xlabel('승률')
    ax.set_title('KBO 팀 누적 승률/순위')

    return fig  # fig 객체 반환

if __name__ == "__main__":
    visualize_team_win_rate()
