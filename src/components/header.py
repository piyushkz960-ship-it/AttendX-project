import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div class="ax-hero" style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:22px; margin-top:26px; text-align:center;">
            <img src='{logo_url}' style='height:96px; margin-bottom:12px; filter: drop-shadow(0 8px 18px rgba(0,0,0,0.25));' />
            <h1 style='margin:0;'>AttendX</h1>
            <p style='margin:6px 0 0 0; font-size:1.05rem; letter-spacing:.02em;'>AI-Powered Attendance, Simplified</p>
        </div>

                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div class="ax-brand" style="display:flex; align-items:center; justify-content:center; gap:12px;">
            <img src='{logo_url}' style='height:56px;' />
            <h2 style='text-align:left;'>AttendX</h2>
        </div>

                """, unsafe_allow_html=True)
