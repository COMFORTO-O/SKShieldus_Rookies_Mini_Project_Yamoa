import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import pandas as pd

def plt_player_record():
    # 폰트 설정
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

    # CSV 파일 불러오기
    batter_record_df = pd.read_csv('../csv/scrap_batter_record.csv', encoding='utf-8').head(15)
    bowler_record_df = pd.read_csv('../csv/scrap_bowler_record.csv', encoding='utf-8').head(15)

    # 타자 그래프
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(y='선수명', x='타율', data=batter_record_df, color='skyblue')
    plt.title('타자 그래프')

    # 막대 오른쪽 숫자 추가
    for i, v in enumerate(batter_record_df['타율']):
        plt.text(v + 0.005, i, f'{v:.3f}', va='center')  # 위치 조정, 소수 3자리

    plt.legend([], [], frameon=False)
    plt.tight_layout()
    plt.show()

    # 투수 그래프
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(y='선수명', x='평균자책점', data=bowler_record_df, color='salmon')
    plt.title('투수 그래프')

    # 막대 오른쪽 숫자 추가
    for i, v in enumerate(bowler_record_df['평균자책점']):
        plt.text(v + 0.1, i, f'{v:.2f}', va='center')

    plt.legend([], [], frameon=False)
    plt.tight_layout()
    plt.show()
