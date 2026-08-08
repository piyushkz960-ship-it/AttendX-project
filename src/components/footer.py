import streamlit as st


def footer_home():

    st.markdown("""
        <div style="margin-top:2.5rem; padding-top:1.25rem; display:flex; justify-content:center; border-top:1px solid rgba(255,255,255,0.18);">
        <p style="font-weight:500; color:#DCDBFF !important; opacity:.85; font-size:.85rem; margin:0;"> Created with ❤️ by Piyush Yadav </p>
        </div>

                """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="margin-top:2.5rem; padding-top:1.25rem; display:flex; justify-content:center; border-top:1px solid var(--ax-border);">
        <p style="font-weight:500; color:var(--ax-muted) !important; font-size:.85rem; margin:0;"> Created with ❤️ by Piyush Yadav </p>
        </div>

                """, unsafe_allow_html=True)
