import streamlit as st

# Internal Style (내부 스타일 시트)
def show():
    st.markdown("""
        <style>
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 2rem;
                background-color: #f0f2f6;
                border-bottom: 1px solid #ccc;
            }
            .logo {
                font-size: 20px;
                font-weight: bold;
                color: black;
                cursor: pointer;
                text-decoration: none;
            }
            .nav-tabs {
                display: flex;
                gap: 3rem;
                margin: 0 auto;
            }
            .nav-tabs a {
                font-size: 15px;
                font-weight: 500;
                color: black;
                text-decoration: none;
                border-bottom: 2px solid transparent;
            }
            .nav-tabs a:hover {
                color: #2c6ef7;
                border-bottom: 2px solid #2c6ef7;
            }
        </style>

        <div class="navbar">
            <a href="/main" target="_self" class="logo"><div class="logo">야모아</div></a>
            <div class="nav-tabs">
                <a href="/today_baseball" target="_self"><span>오늘의야구</span></a>
                <a href="/entry_guide" target="_self"><span>입덕가이드</span></a>
            </div>
            <div></div>
        </div>
    """, unsafe_allow_html=True)
