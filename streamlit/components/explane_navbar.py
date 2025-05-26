import streamlit as st
from PIL import Image
import base64
import os

def show(num):
    # 이미지 불러오기 및 base64 인코딩
    file_path = "../assets/로고 배경 없음.jpeg"
    with open(file_path, "rb") as f:
        image_bytes = f.read()
        encoded = base64.b64encode(image_bytes).decode()

    image_uri = f"data:image/jpeg;base64,{encoded}"

    if num == 1:
        st.markdown(f"""
            <style>
                .navbar {{
                    width: 100%;
                    padding: 1rem 2rem;
                    background-color: #ffffff;
                    border: 1px solid #e0e0e0;
                    display: flex;
                    align-items: center;
                }}
                .navbar-logo {{
                    height: 60px;
                    margin-right: 10px;
                }}
                .navbar-title {{
                    font-size: 20px;
                    font-weight: bold;
                    color: #1f2937;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }}
            </style>

            <div class="navbar">
                <img class="navbar-logo" src="{image_uri}" alt="야모아 로고">
                <div class="navbar-title">메인 - 팀별 승수, 팀별 순위 변화, 선수 기록 그래프화</div>
            </div>
        """, unsafe_allow_html=True)

    elif num == 2:
        st.markdown(f"""
            <style>
                .navbar {{
                    width: 100%;
                    padding: 1rem 2rem;
                    background-color: #ffffff;
                    border: 1px solid #e0e0e0;
                    display: flex;
                    align-items: center;
                }}
                .navbar-logo {{
                    height: 60px;
                    margin-right: 10px;
                }}
                .navbar-title {{
                    font-size: 20px;
                    font-weight: bold;
                    color: #1f2937;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }}
            </style>

            <div class="navbar">
                <img class="navbar-logo" src="{image_uri}" alt="야모아 로고">
                <div class="navbar-title">오늘의 야구 - 오늘의 야구 경기와 관련된 다양한 정보를 확인</div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
            <style>
                .navbar {{
                    width: 100%;
                    padding: 1rem 2rem;
                    background-color: #ffffff;
                    border: 1px solid #e0e0e0;
                    display: flex;
                    align-items: center;
                }}
                .navbar-logo {{
                    height: 60px;
                    margin-right: 10px;
                }}
                .navbar-title {{
                    font-size: 20px;
                    font-weight: bold;
                    color: #1f2937;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }}
            </style>

            <div class="navbar">
                <img class="navbar-logo" src="{image_uri}" alt="야모아 로고">
                <div class="navbar-title">입덕 가이드 - 야구에 관심 두기 시작한 분들을 위한 기능 제공</div>
            </div>
        """, unsafe_allow_html=True)
