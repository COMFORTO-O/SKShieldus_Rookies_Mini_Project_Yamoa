import pandas as pd
import os

def dataset_matchup():

    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, '..', 'csv')

    # CSV 파일 불러오기
    try:
        csv_file = os.path.join(csv_path, 'scrap_match_up_main.csv')
        df_main = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("❌ CSV 파일을 찾을 수 없어요! 경로를 다시 확인해줘요!")
        exit()
        


    # 야구장별 홈팀 추론용 매핑
    stadium_home_team_map = {
        "잠실": "두산",
        "잠실": "LG",
        "문학": "SSG",
        "대구": "삼성",
        "고척": "키움",
        "대전(신)": "한화",
        "창원": "NC",
        "수원": "KT",
        "광주": "KIA",
        "부산": "롯데",
        "청주": "한화",
        "울산": "롯데",
        "사직" : "롯데"
    }

    def save_game_by_row(row):
        stadium = row['야구장']
        home_team = stadium_home_team_map.get(stadium)

        if not home_team:
            print(f"⚠️ 알 수 없는 홈팀 경기장: {stadium}")
            return

        # 홈팀 / 원정팀 정리
        if row['팀명1'] == home_team:
            home = {
                'team': row['팀명1'],
                'pitcher': row['선발투수1'],
                'pitcher_era': pd.to_numeric(row['선발투수1 AVG'], errors='coerce'),
                'pitcher_war': pd.to_numeric(row['선발투수1 WAR'], errors='coerce'),
                'batting_avg': pd.to_numeric(row['팀 BA 1'], errors='coerce')
            }
            away = {
                'team': row['팀명2'],
                'pitcher': row['선발투수2'],
                'pitcher_era': pd.to_numeric(row['선발투수2 AVG'], errors='coerce'),
                'pitcher_war': pd.to_numeric(row['선발투수2 WAR'], errors='coerce'),
                'batting_avg': pd.to_numeric(row['팀 BA 2'], errors='coerce')
            }
        else:
            home = {
                'team': row['팀명2'],
                'pitcher': row['선발투수2'],
                'pitcher_era': pd.to_numeric(row['선발투수2 AVG'], errors='coerce'),
                'pitcher_war': pd.to_numeric(row['선발투수2 WAR'], errors='coerce'),
                'batting_avg': pd.to_numeric(row['팀 BA 2'], errors='coerce')
            }
            away = {
                'team': row['팀명1'],
                'pitcher': row['선발투수1'],
                'pitcher_era': pd.to_numeric(row['선발투수1 AVG'], errors='coerce'),
                'pitcher_war': pd.to_numeric(row['선발투수1 WAR'], errors='coerce'),
                'batting_avg': pd.to_numeric(row['팀 BA 1'], errors='coerce')
            }

        new_games = pd.DataFrame([{
            'home_team': home['team'],
            'away_team': away['team'],
            'home_pitcher': home['pitcher'],
            'away_pitcher': away['pitcher'],
            'home_pitcher_era': home['pitcher_era'],
            'away_pitcher_era': away['pitcher_era'],
            'home_pitcher_war': home['pitcher_war'],
            'away_pitcher_war': away['pitcher_war'],
            'home_batting_avg': home['batting_avg'],
            'away_batting_avg': away['batting_avg']
        }])

        csv_filename = f"new_games_{home['team'].upper()}.csv"
        new_games.to_csv(os.path.join(csv_path, csv_filename), index=False, encoding='utf-8-sig')

        # new_games.to_csv(csv_path, csv_filename, index=False)
        print(f"✅ [{home['team']}] 경기 저장 완료: {csv_filename}")

    # 모든 행에 대해 저장 수행
    if df_main.empty:
        print("❌ 데이터가 비어 있어요! CSV 내용을 확인해주세요!")
    else:
        for _, row in df_main.iterrows():
            save_game_by_row(row)
        print("🎉 모든 경기가 저장 완료되었어요!")
        return
