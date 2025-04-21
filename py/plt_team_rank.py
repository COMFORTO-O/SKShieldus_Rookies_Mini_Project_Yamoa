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
    
# <<<<<<< HEAD
    df_team = pd.read_csv('../csv/scrap_team_rank.csv')
# =======
    df_team = pd.read_csv(csv_path)
# >>>>>>> origin/feature/win_rate_prediction

    # 승률 기준으로 오름차순 정렬
    df_team = df_team.sort_values(by='승률', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 7))  # 새로운 figure와 ax 객체 생성

    x = range(len(df_team))
    draw_rate = 1 - df_team['승률'] - df_team['패배율']
    df_team['무승부율'] = draw_rate

    plt.bar(x, df_team['승률'], label='승률', color='pink')
    plt.bar(x, df_team['무승부율'], bottom=df_team['승률'], label='무승부율', color='lightgray')
    plt.bar(x, df_team['패배율'], bottom=df_team['승률'] + df_team['무승부율'], label='패배율', color='skyblue')

    plt.xticks(x, df_team['팀명'])

    # 값 표시
    for i, rate in enumerate(df_team['승률']):
        total = df_team.loc[i, ['승률', '무승부율', '패배율']].sum()
        plt.text(i, total - 0.5, f'{rate:.3f}%', ha='center', fontsize=10, color='black')

    # plot 특징 수정
    plt.legend(loc='upper right')
    plt.ylim(0, 1.0)
    # plt.yticks(np.arange(0, 28, 3))
    plt.xlabel('팀명')
    plt.ylabel('승률')
    plt.title('KBO 팀 누적 승률/순위')
    plt.show()

if __name__ == "__main__":
    visualize_team_win_rate()
