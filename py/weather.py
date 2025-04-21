import httpx
import ssl
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

def weather_today(field_name):
    field_list = [
        '27230510', #대구
        '48160720', #마산
        '26260590', #사직
        '11470510', #목동
        '11710720', #잠실
        '28170740', #문학
        '45130680', #월명
        '29170570', #무등
        '43113630', #청주
        '30140640' #한밭
        ]

    areas_list = []

    for code in field_list:
        url = f"https://wwwnew.kweather.co.kr/forecast/data/lifestyle/{code}.xml"

        # SSL 설정: 보안 수준 낮춤
        context = ssl.create_default_context()
        context.set_ciphers("DEFAULT:@SECLEVEL=1")  # 보안 레벨 1로 낮춤

        try:
            with httpx.Client(verify=context, timeout=10.0) as client:
                response = client.get(url)
                response.encoding = 'utf-8'
                #print(response.text)
                soup = BeautifulSoup(response.text, features='xml')
                

            # 상단 지역 정보 추출
            area_info = {
                "areaCode": soup.find("areaCode").text,
                "areaName1": soup.find("areaName1").text,
                "areaName2": soup.find("areaName2").text,
                "areaName3": soup.find("areaName3").text,
                "announceTime": soup.find("announceTime").text,
            }

            # 날씨 데이터 리스트
            weather_data = []
            # Initialize empty lists for each key
            time_list = []
            weather_list = []
            temp_list = []
            rainProb_list = []

            day = soup.find("day")  # 첫 번째 day 태그만 선택

            day_data = {
                "applyDate": day.find("applyDate").text,
                "weather": day.find("weather").text,
                "tempMin": int(day.find("tempMin").text),
                "tempMax": int(day.find("tempMax").text),
                "rainProb": int(day.find("rainProb").text),
                "hours": []
            }

            # 시간별 hours
            for h in day.find_all("hour"):
                day_data["hours"].append({
                "time": int(h.find("time").text),
                "weather": h.find("weather").text,
                "temp": int(h.find("temp").text),
                "rainProb": int(h.find("rainProb").text),
                })
            
            weather_data.append(day_data)

            # Iterate through weather_data
            for day in weather_data:
                for hour in day['hours']:
                    time_list.append(hour['time'])
                    weather_list.append(hour['weather'])
                    temp_list.append(hour['temp'])
                    rainProb_list.append(hour['rainProb'])


            area_info["time"] = time_list
            area_info["weather"] = weather_list
            area_info["temp"] = temp_list
            area_info["rainProb"] = rainProb_list
        
            areas_list.append(area_info)
            

        except Exception as e:
            print(f"Error occurred: {e}")
            continue
        finally:
            context = None

    # Initialize empty lists for each key
    time_list = []
    weather_list = []
    temp_list = []
    rainProb_list = []

    # Iterate through weather_data
    for day in weather_data:
        for hour in day['hours']:
            time_list.append(hour['time'])
            weather_list.append(hour['weather'])
            temp_list.append(hour['temp'])
            rainProb_list.append(hour['rainProb'])

    areas_weather_df = pd.DataFrame(areas_list)
    areas_weather_df.to_csv('scrap_weather_today.csv', index=False, encoding='utf-8-sig')

    # 한글 폰트 설정
    font_path = 'C:\\windows\\Fonts\\malgun.ttf'
    font_prop = fm.FontProperties(fname=font_path).get_name()
    matplotlib.rc('font', family=font_prop)

    stadium_list = {
        '대구야구장': '27230510',  # 대구
        '마산야구장': '48160720',  # 마산
        '사직야구장': '26260590',  # 사직
        '목동야구장': '11470510',  # 목동
        '잠실야구장': '11710720',  # 잠실
        '문학야구장': '28170740',  # 문학
        '월명야구장': '45130680',  # 월명
        '무등야구장': '29170570',  # 무등
        '청주야구장': '43113630',  # 청주
        '한밭야구장': '30140640'   # 한밭
    }

    stadium_list = {k: int(v) for k, v in stadium_list.items()}
    areaCode = stadium_list[field_name]
    # CSV 불러오기
    areas_weather_today_df = pd.read_csv('scrap_weather_today.csv')
    area_weather_today_df = areas_weather_today_df[areas_weather_today_df['areaCode'] == areaCode] # 특정 야구장 날씨만 가져오기

    time_list = area_weather_today_df['time'].iloc[0]
    rainProb_list = area_weather_today_df['rainProb'].iloc[0]
    temp_list = area_weather_today_df['temp'].iloc[0]

    # Convert strings to lists
    time_list = eval(time_list)
    rainProb_list = eval(rainProb_list)
    temp_list = eval(temp_list)

    # Create a DataFrame for plotting
    df_plot = pd.DataFrame({
        '시간': time_list,
        '강수 확률': rainProb_list,
        '기온': temp_list
    })

    # 스타일
    sns.set_palette("pastel")

    # 그래프 생성
    fig, ax1 = plt.subplots(figsize=(10, 6))

    filtered_df_plot = df_plot[(df_plot['시간'] >= 14) & (df_plot['시간'] <= 22)]

    # 강수 확률 막대 그래프
    bars = sns.barplot(data=filtered_df_plot, x='시간', y='강수 확률', color='skyblue', ax=ax1)
    # Update x-axis labels to include '시' and remove the x-axis title
    ax1.set_xlabel('')
    ax1.set_xticks(range(len(filtered_df_plot['시간'])))
    ax1.set_xticklabels([f"{hour}시" for hour in filtered_df_plot['시간']])

    ax1.set_ylabel('강수 확률 (%)', color='skyblue')
    ax1.set_ylim(0, 100)
    ax1.tick_params(axis='y', labelcolor='skyblue')

    for bar in bars.patches:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height:.0f}', 
                ha='center', va='bottom', fontsize=10, color='skyblue')

    # 기온 꺾은선 그래프
    ax2 = ax1.twinx()

    # Adjust x-axis alignment for the line plot
    ax2.plot(range(len(filtered_df_plot['시간'])), filtered_df_plot['기온'], marker='o', color='red', label='기온', linewidth=2)

    # Update text annotations for the adjusted x-axis
    for i, val in enumerate(filtered_df_plot['기온']):
        ax2.text(i, val + 0.8, f'{val:.0f}', ha='center', va='bottom', fontsize=10, color='red')

    ax2.set_ylabel('기온 (°C)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(0, 35)

    

    # 제목
    plt.title(f'{field_name} 오늘의 날씨')

    # axes 선 제거 (양쪽)
    for spine in ['top', 'right', 'left', 'bottom']:
        ax1.grid(False)
        ax2.grid(False)

    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.show()

    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.show()



weather_today('대구야구장')