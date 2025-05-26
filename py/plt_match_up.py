import pandas as pd
import matplotlib.pyplot as plt
import os

def plt_match_up(home_team_name, away_team_name):

    base_path = os.path.dirname(__file__)
    csv_path_main = os.path.join(base_path, '..', 'csv', 'scrap_match_up_main.csv')
    csv_path_ml = os.path.join(base_path, '..', 'csv', 'oddsofwinning_ml.csv')


    # 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

    # CSV 불러오기
    df_main = pd.read_csv(csv_path_main, encoding='utf-8-sig')
    odds_df = pd.read_csv(csv_path_ml, encoding='utf-8-sig')
    # home_team_name에 해당하는 데이터만 필터링
    df_main = df_main[df_main['팀명1'] == home_team_name]
    row = df_main.iloc[0]
    odds_df = odds_df[odds_df['home_team'] == home_team_name]
    row_odds = odds_df.iloc[0]

    print(df_main)

    # 색상 지정
    bar_color = '#a32035'

    # 기준값 설정
    max_ba = 0.4
    max_era = 30.0
    max_win_rate = 1.0

    # 팀 정보 및 지표 추출
    home_team = row['팀명1']
    away_team = row['팀명2']
    
    team_1_ba = row['팀 BA 1'] 
    team_2_ba = row['팀 BA 2'] 
    
    starting_line_up_avg_1 = row['선발투수1 AVG'] 
    starting_line_up_avg_2 = row['선발투수2 AVG'] 

    win_rate_1 = row_odds['home_winrate']
    win_rate_2 = row_odds['away_winrate']

    # 정규화
    norm_team_1_ba = team_1_ba / max_ba
    norm_team_2_ba = team_2_ba / max_ba
    
    norm_era_1 = 1 - (starting_line_up_avg_1 / max_era)
    norm_era_2 = 1 - (starting_line_up_avg_2 / max_era)
    
    norm_win_rate_1 = row_odds['home_winrate'] / max_win_rate
    norm_win_rate_2 = row_odds['away_winrate'] / max_win_rate

    # 정규화된 값
    values_1 = [norm_win_rate_1, norm_team_1_ba, norm_era_1]
    values_2 = [norm_win_rate_2, norm_team_2_ba, norm_era_2]
    
    # 실제 표시할 원래 값
    raw_values_1 = [win_rate_1, team_1_ba, starting_line_up_avg_1]
    raw_values_2 = [win_rate_2, team_2_ba, starting_line_up_avg_2]
    
    labels = ['승률', '팀 타율', '선발선수 평균자책']

    # 순서 뒤집기
    labels = labels[::-1]
    values_1 = values_1[::-1]
    values_2 = values_2[::-1]
    raw_values_1 = raw_values_1[::-1]
    raw_values_2 = raw_values_2[::-1]

    # 홈팀 그래프
    fig1, ax = plt.subplots(figsize=(7, 3))
    ax.barh(labels, values_1, color=bar_color, height=0.4)
    ax.set_yticks([])  # y축 레이블 제거
    for j, value in enumerate(values_1):
        ax.text(value + 0.1, j, f'{raw_values_1[j]:.3f}', va='center', ha='left', fontsize=20, fontweight='bold')
    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax.tick_params(left=False, bottom=False)
    ax.set_xticks([])
    ax.grid(False)
    ax.invert_xaxis()
    plt.tight_layout()


    # 어웨이팀 그래프
    fig2, ax = plt.subplots(figsize=(7, 3))
    ax.barh(labels, values_2, color=bar_color, height=0.4)
    for j, value in enumerate(values_2):
        ax.text(value + 0.01, j, f'{raw_values_2[j]:.3f}', va='center', ha='left', fontsize=20, fontweight='bold')
    ax.set_yticks([])  # y축 레이블 제거
    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax.tick_params(left=False, bottom=False)
    ax.set_xticks([])
    ax.grid(False)
    plt.tight_layout()
    
    return fig1, fig2  # fig 객체 반환

