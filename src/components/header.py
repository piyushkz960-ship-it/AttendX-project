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
        <div class="ax-brand" style="display:flex; align-items:center; justify-content:flex-start; gap:12px;">
            <img src='{logo_url}' style='height:56px;' />
            <h2 style='text-align:left;'>AttendX</h2>
        </div>

                """, unsafe_allow_html=True)


def user_badge(name, role):
    initials = "".join(part[0] for part in name.split()[:2]).upper() or "?"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-end; gap:12px;">
            <div style="text-align:right;">
                <div style="font-family:'Poppins', sans-serif; font-weight:700; color:var(--ax-ink); font-size:1.05rem; line-height:1.25;">{name}</div>
                <div style="color:var(--ax-muted); font-size:.75rem; text-transform:uppercase; letter-spacing:.06em;">{role}</div>
            </div>
            <div class="ax-avatar">{initials}</div>
        </div>

                """, unsafe_allow_html=True)
