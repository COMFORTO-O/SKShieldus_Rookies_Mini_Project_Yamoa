
def predict_winrate(home_team, away_team):
    
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    import os
    import glob
    import matplotlib
    import matplotlib.pyplot as plt
    from PIL import Image
    import matplotlib.font_manager as fm
    import pandas as pd


    # 1. 학습용 데이터
    data = pd.DataFrame({
        'home_pitcher_era': [2.45, 3.12, 4.01, 3.95, 3.30, 2.85, 3.73, 2.67, 3.95, 4.10, 3.40, 3.58, 2.71, 3.85, 2.35, 4.45, 2.95, 3.11, 2.82, 3.48,3.22, 2.55, 3.97, 4.33, 3.27, 3.12, 2.74, 2.89, 3.64, 3.99, 3.55, 3.78, 2.55, 3.50, 2.66, 3.93, 3.88, 3.10, 2.81,3.45, 3.89, 2.77, 3.60, 4.10, 3.56, 2.84, 2.96, 3.25, 3.90, 3.25],
        'away_pitcher_era': [3.45, 4.11, 3.33, 2.85, 2.90, 2.75, 4.01, 3.55, 3.88, 3.80, 2.73, 4.10, 3.65, 2.55, 2.90, 3.75, 3.60, 4.33, 3.95, 4.01,3.78, 3.22, 3.91, 2.99, 4.35, 3.75, 3.40, 4.22, 3.20, 4.11, 3.55, 3.25, 4.05, 3.66, 4.44, 3.20, 3.92, 4.01, 3.80,4.25, 3.91, 2.97, 3.82, 3.55, 2.87, 3.61, 3.77, 3.50, 3.42, 3.50],
        'home_pitcher_war': [4.10, 3.22, 3.55, 4.23, 3.80, 3.75, 3.90, 3.50, 4.10, 4.00, 3.66, 3.33, 4.20, 3.72, 3.88, 3.90, 4.15, 3.77, 4.35, 4.22, 3.56, 3.91, 4.26, 3.75, 4.00, 3.78, 3.65, 3.22, 3.40, 4.11, 3.55, 4.08, 3.88, 4.15, 4.00, 3.95, 4.21, 3.17, 3.90,4.11, 3.93, 3.11, 4.22, 3.55, 3.82, 3.91, 4.15, 3.45, 3.91, 3.45],
        'away_pitcher_war': [3.66, 3.11, 2.99, 3.55, 3.80, 3.72, 3.62, 3.40, 3.88, 3.33, 4.12, 3.88, 3.75, 4.10, 3.66, 3.55, 2.78, 3.25, 3.09, 3.88, 3.33, 3.45, 3.66, 3.99, 3.55, 3.88, 3.22, 3.72, 3.45, 3.60, 4.11, 3.40, 3.50, 3.66, 3.35, 3.77, 4.22, 3.12, 3.99, 3.55, 3.88, 4.11, 3.72, 4.33, 4.08, 4.12, 3.40, 4.24, 3.40, 3.72],
        'home_batting_avg': [0.288, 0.265, 0.270, 0.285, 0.290, 0.273, 0.278, 0.270, 0.295, 0.280, 0.268, 0.273, 0.275, 0.286, 0.293, 0.290, 0.265, 0.267, 0.275, 0.272, 0.280, 0.278, 0.290, 0.285, 0.274, 0.276, 0.268, 0.270, 0.285, 0.284, 0.267, 0.278, 0.289, 0.275, 0.293, 0.283, 0.290, 0.292, 0.288, 0.276, 0.284, 0.275, 0.277, 0.290, 0.285, 0.274, 0.289, 0.278, 0.275, 0.289],
        'away_batting_avg': [0.273, 0.290, 0.265, 0.285, 0.278, 0.288, 0.274, 0.286, 0.264, 0.276, 0.290, 0.274, 0.280, 0.288, 0.270, 0.265, 0.274, 0.281, 0.268, 0.270, 0.278, 0.285, 0.265, 0.274, 0.289, 0.265, 0.270, 0.276, 0.278, 0.285, 0.283, 0.270, 0.280, 0.290, 0.278, 0.277, 0.273, 0.281, 0.280, 0.268, 0.283, 0.277, 0.287, 0.268, 0.275, 0.286, 0.265, 0.270, 0.278, 0.289],
        'winrate_diff': [0.12, -0.25, 0.18, -0.22, 0.15, 0.13, 0.18, -0.28, 0.22, -0.2, 0.11, 0.14, 0.18, -0.21, -0.27, 0.15, 0.17, 0.12, -0.29, 0.25, 0.15, -0.22, 0.28, -0.18, 0.21, 0.19, -0.26, 0.17, -0.19, 0.27, -0.29, 0.14, 0.11, -0.28, 0.19, -0.16, 0.13, -0.21, 0.17, 0.11, -0.29, -0.18, 0.26, -0.22, 0.15, 0.14, 0.18, -0.20, 0.24, 0.14]
    })

    features = [
        'home_pitcher_era', 'away_pitcher_era',
        'home_pitcher_war', 'away_pitcher_war',
        'home_batting_avg', 'away_batting_avg'
    ]

    # 2. 회귀 모델 학습 (스케일러 포함 파이프라인)
    model = make_pipeline(StandardScaler(), RandomForestRegressor(n_estimators=100, random_state=42))
    model.fit(data[features], data['winrate_diff'])

    # 3. 예측 함수 정의
    def predict_winrate(input_df: pd.DataFrame):
        predicted_diff = model.predict(input_df[features])

        # 예측된 승률 차이로부터 홈/원정 승률 계산
        home_winrate = (predicted_diff + 1) / 2
        away_winrate = 1 - home_winrate

        result_df = input_df.copy()
        result_df['predicted_winrate_diff'] = predicted_diff
        result_df['home_winrate'] = home_winrate
        result_df['away_winrate'] = away_winrate

        return result_df[['predicted_winrate_diff', 'home_winrate', 'away_winrate']]


    # 4. 새로운 경기 예측

    csv_files = glob.glob(os.path.join('../csv/', 'new_games*.csv'))
    new_games = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

    # Extract the first four columns from the original new_games DataFrame
    metadata_columns = ['home_team', 'away_team', 'home_pitcher', 'away_pitcher']
    metadata = new_games[metadata_columns] if all(col in new_games.columns for col in metadata_columns) else None

    # 메타데이터 제거 후 nea_games DataFrame 생성
    new_games = new_games.drop(columns=metadata_columns)

    # 경기 예측
    predicted = predict_winrate(new_games)

    predicted = pd.concat([metadata.reset_index(drop=True), predicted.reset_index(drop=True)], axis=1)
    predicted.to_csv('../csv/oddsofwinning_ml.csv', index=False, encoding='utf-8-sig')

    # 한글 폰트 설정
    font_path = 'C:\\windows\\Fonts\\malgun.ttf'
    font_prop = fm.FontProperties(fname=font_path).get_name()
    matplotlib.rc('font', family=font_prop)

    # CSV 파일을 데이터프레임으로 읽기
    odds_df = pd.read_csv('../csv/oddsofwinning_ml.csv')

    for index, row in odds_df.iterrows():
        home_team = row['home_team']
        away_team = row['away_team']
        home_winrate = row['home_winrate'] * 100
        away_winrate = row['away_winrate'] * 100

        # 이미지 경로 수정
        home_img = Image.open(f"../jpg/{home_team}.jpg")
        away_img = Image.open(f"../jpg/{away_team}.jpg")

        # 전체 그림
        fig = plt.figure(figsize=(14, 5))

        # 제목
        plt.text(0.5, 0.95, f"{home_team} vs {away_team} 승부예측", ha='center', va='center', fontsize=17, color='black', weight='bold', transform=fig.transFigure)

        # 왼쪽 이미지
        ax_img_home = fig.add_axes([0.05, 0.25, 0.2, 0.5])
        ax_img_home.imshow(home_img)
        ax_img_home.axis('off')

        # 오른쪽 이미지
        ax_img_away = fig.add_axes([0.75, 0.25, 0.2, 0.5])
        ax_img_away.imshow(away_img)
        ax_img_away.axis('off')

        # 중앙 그래프
        ax_bar = fig.add_axes([0.3, 0.4, 0.4, 0.2])


        # 팀별 색상 딕셔너리
        team_colors = {
            '키움': '#570514',
            '두산': '#1A1748',
            '롯데': '#041E42',
            '삼성': '#074CA1',
            '한화': '#FC4E00',
            'KIA': '#EA0029',
            'LG': '#C30452',
            'SSG': '#FFB81C',
            'NC': '#315288',
            'KT': '#EB1C24' 
        }

        # 중앙 그래프 색상 설정
        home_color = team_colors.get(home_team, '#1f77b4')  # 기본값: 진한 파랑
        away_color = team_colors.get(away_team, '#00cfff')  # 기본값: 밝은 하늘색

        ax_bar.barh(0, home_winrate, color=home_color, height=0.6)
        ax_bar.barh(0, away_winrate, left=home_winrate, color=away_color, height=0.6)

        # 승률 텍스트
        ax_bar.text(home_winrate / 2, 0, f"{home_winrate:.1f}%", va='center', ha='center', color='white', fontsize=14, weight='bold')
        ax_bar.text(home_winrate + away_winrate / 2, 0, f"{away_winrate:.1f}%", va='center', ha='center', color='white', fontsize=14, weight='bold')    

        # 축과 눈금 완전 제거
        ax_bar.axis('off')
        ax_bar.set_xticks([])
        ax_bar.set_yticks([])
        for spine in ax_bar.spines.values():
            spine.set_visible(False)

        ax_bar.set_xlim(0, 100)

        # 특정 팀에 대한 그래프만 표시
        if home_team == '두산' and away_team == 'KIA':
            plt.show()
        else:
            plt.close(fig)

        # plt.show()


predict_winrate('두산', 'KIA')