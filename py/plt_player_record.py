import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plt_player_record():
    # 폰트 설정
    plt.rc('font', family='Malgun Gothic')  # 폰트 설정
    plt.rcParams['axes.unicode_minus'] = False

    base_path = os.path.dirname(__file__)
    csv_path1 = os.path.join(base_path, '..', 'csv', 'scrap_batter_record.csv')
    csv_path2 = os.path.join(base_path, '..', 'csv', 'scrap_bowler_record.csv')

    # CSV 파일 불러오기
    batter_record_df = pd.read_csv(csv_path1, encoding='utf-8').head(15)
    bowler_record_df = pd.read_csv(csv_path2, encoding='utf-8').head(15)

    # 타자 그래프
    fig, ax = plt.subplots(figsize=(10, 6))  # figure와 ax 객체 생성
    sns.barplot(y='선수명', x='타율', data=batter_record_df, color='skyblue', ax=ax)  # ax에 시각화
    ax.set_title('타자 그래프')

    # 막대 오른쪽 숫자 추가
    for i, v in enumerate(batter_record_df['타율']):
        ax.text(v + 0.005, i, f'{v:.3f}', va='center')  # 위치 조정, 소수 3자리

    ax.legend([], [], frameon=False)
    plt.tight_layout()

    # 투수 그래프
    fig2, ax2 = plt.subplots(figsize=(10, 6))  # figure와 ax 객체 생성
    sns.barplot(y='선수명', x='평균자책점', data=bowler_record_df, color='salmon', ax=ax2)  # ax에 시각화
    ax2.set_title('투수 그래프')

    # 막대 오른쪽 숫자 추가
    for i, v in enumerate(bowler_record_df['평균자책점']):
        ax2.text(v + 0.1, i, f'{v:.2f}', va='center')

    ax2.legend([], [], frameon=False)
    plt.tight_layout()

    # 두 그래프를 하나의 figure에 넣어서 반환
    return fig, fig2
