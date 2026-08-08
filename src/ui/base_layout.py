import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: radial-gradient(120% 140% at 15% 0%, #4F46E5 0%, #4338CA 45%, #211E52 100%) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: var(--ax-surface) !important;
                    padding: 2.75rem 2.25rem !important;
                    border-radius: var(--ax-radius-lg) !important;
                    box-shadow: var(--ax-shadow-lg) !important;
                    text-align: center !important;
                    transition: transform .25s ease, box-shadow .25s ease !important;
                }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-6px) !important;
                    box-shadow: var(--ax-shadow-xl) !important;
                }

                .stApp div[data-testid="stColumn"] .stImage {
                    display: flex !important;
                    justify-content: center !important;
                    margin: .25rem 0 1.1rem 0 !important;
                }

                .stApp div[data-testid="stColumn"] .stButton {
                    display: flex !important;
                    justify-content: center !important;
                    margin-top: .5rem !important;
                }

                .stApp div[data-testid="stColumn"] h2 {
                    color: var(--ax-ink) !important;
                }
        </style>

                """
            ,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: var(--ax-bg) !important;
                }

        </style>

                """
            ,unsafe_allow_html=True)




def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        :root {
            --ax-primary: #4F46E5;
            --ax-primary-dark: #4338CA;
            --ax-primary-light: #EEF2FF;
            --ax-secondary: #0D9488;
            --ax-secondary-dark: #0F766E;
            --ax-ink: #1E293B;
            --ax-muted: #64748B;
            --ax-bg: #F5F6FB;
            --ax-surface: #FFFFFF;
            --ax-border: #E2E8F0;
            --ax-radius-sm: 10px;
            --ax-radius-md: 14px;
            --ax-radius-lg: 26px;
            --ax-shadow: 0 2px 10px rgba(30, 41, 59, 0.06);
            --ax-shadow-lg: 0 10px 30px rgba(30, 41, 59, 0.10);
            --ax-shadow-xl: 0 18px 40px rgba(30, 41, 59, 0.16);
        }

         /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.75rem !important;
                max-width: 1100px !important;
            }

            h1 {
                font-family: 'Poppins', sans-serif !important;
                font-size: 3.2rem !important;
                font-weight: 700 !important;
                line-height: 1.15 !important;
                margin-bottom: 0.4rem !important;
                color: var(--ax-ink) !important;
            }


            h2 {
                font-family: 'Poppins', sans-serif !important;
                font-size: 1.7rem !important;
                font-weight: 700 !important;
                line-height: 1.25 !important;
                margin-bottom: 0.3rem !important;
                color: var(--ax-ink) !important;
            }

            h3, h4, p, label {
                font-family: 'Outfit', sans-serif !important;
            }

            [data-testid="stIconMaterial"] {
                font-family: 'Material Symbols Rounded' !important;
            }

            h3, h4 {
                color: var(--ax-ink) !important;
            }

            p, label {
                color: var(--ax-muted) !important;
            }

            input, textarea {
                font-family: 'Outfit', sans-serif !important;
            }

            /* ---------- Buttons ---------- */

            .stButton > button{
                border-radius: var(--ax-radius-sm) !important;
                background-color: var(--ax-primary) !important;
                color: white !important;
                font-weight: 600 !important;
                padding: 10px 22px !important;
                border: none !important;
                box-shadow: var(--ax-shadow) !important;
                transition: transform 0.18s ease, box-shadow 0.18s ease, background-color 0.18s ease !important;
                }

            .stButton > button:hover{
                transform: translateY(-2px) !important;
                background-color: var(--ax-primary-dark) !important;
                box-shadow: var(--ax-shadow-lg) !important;
                }

            .stButton > button[kind="secondary"]{
                background-color: var(--ax-secondary) !important;
                color: white !important;
                }

            .stButton > button[kind="secondary"]:hover{
                background-color: var(--ax-secondary-dark) !important;
                }

            .stButton > button[kind="tertiary"]{
                background-color: var(--ax-surface) !important;
                color: var(--ax-ink) !important;
                border: 1.5px solid var(--ax-border) !important;
                box-shadow: none !important;
                }

            .stButton > button[kind="tertiary"]:hover{
                border-color: var(--ax-primary) !important;
                color: var(--ax-primary) !important;
                background-color: var(--ax-primary-light) !important;
                }

            .stButton > button:disabled{
                opacity: 0.45 !important;
                transform: none !important;
                box-shadow: none !important;
                }

            .stButton > button p {
                color: inherit !important;
                font-weight: 600 !important;
                }

            /* ---------- Inputs ---------- */

            .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
                border-radius: var(--ax-radius-sm) !important;
                border: 1.5px solid var(--ax-border) !important;
                background-color: var(--ax-surface) !important;
            }

            .stTextInput input:focus, .stTextArea textarea:focus {
                border-color: var(--ax-primary) !important;
                box-shadow: 0 0 0 3px var(--ax-primary-light) !important;
            }

            [data-testid="stCameraInput"], [data-testid="stFileUploader"], [data-testid="stAudioInput"] {
                border-radius: var(--ax-radius-md) !important;
                overflow: hidden !important;
            }

            [data-testid="stFileUploaderDropzone"] {
                border-radius: var(--ax-radius-md) !important;
                border: 1.5px dashed var(--ax-border) !important;
                background-color: var(--ax-primary-light) !important;
            }

            /* ---------- Misc containers ---------- */

            [data-testid="stDataFrame"] {
                border-radius: var(--ax-radius-md) !important;
                overflow: hidden !important;
                border: 1px solid var(--ax-border) !important;
            }

            hr, [data-testid="stDivider"] {
                border-color: var(--ax-border) !important;
                margin: 1.25rem 0 !important;
            }

            [data-testid="stAlert"] {
                border-radius: var(--ax-radius-sm) !important;
            }

            [data-testid="stAlert"] p {
                color: inherit !important;
            }

            [data-testid="stImage"] img {
                border-radius: var(--ax-radius-sm) !important;
            }

            /* ---------- Dialogs / Modals ---------- */

            [data-testid="stDialog"] > div {
                border-radius: var(--ax-radius-lg) !important;
                box-shadow: var(--ax-shadow-xl) !important;
            }

            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2 {
                color: var(--ax-primary) !important;
                font-family: 'Poppins', sans-serif !important;
            }

            [data-testid="stDialog"] h3,
            [data-testid="stDialog"] h4,
            [data-testid="stDialog"] p {
                color: var(--ax-ink) !important;
                font-family: 'Outfit', sans-serif !important;
            }

            [data-testid="stDialog"] label {
                color: var(--ax-muted) !important;
                font-family: 'Outfit', sans-serif !important;
            }

            /* ---------- Brand header / hero ---------- */

            .ax-hero h1 {
                color: white !important;
            }

            .ax-hero p {
                color: #DCDBFF !important;
            }

            .ax-brand h2 {
                color: var(--ax-primary) !important;
                margin-bottom: 0 !important;
            }

            /* ---------- Card containers (st.container(key="ax_card_...")) ---------- */

            div[class*="st-key-ax_card"] {
                background-color: var(--ax-surface) !important;
                border: 1px solid var(--ax-border) !important;
                border-radius: var(--ax-radius-md) !important;
                padding: 1.5rem 1.75rem !important;
                box-shadow: var(--ax-shadow) !important;
                margin-bottom: 1rem !important;
            }

            /* ---------- Segmented tab bar (st.container(key="ax_tabbar")) ---------- */

            div[class*="st-key-ax_tabbar"] {
                background-color: var(--ax-primary-light) !important;
                border-radius: var(--ax-radius-md) !important;
                padding: 6px !important;
                margin-bottom: 1.25rem !important;
            }

            div[class*="st-key-ax_tabbar"] .stButton > button[kind="tertiary"] {
                background-color: transparent !important;
                border: none !important;
                color: var(--ax-muted) !important;
            }

            div[class*="st-key-ax_tabbar"] .stButton > button[kind="tertiary"]:hover {
                background-color: rgba(255, 255, 255, 0.7) !important;
                color: var(--ax-primary) !important;
            }

            div[class*="st-key-ax_tabbar"] .stButton > button[kind="primary"] {
                box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25) !important;
            }

            /* ---------- Avatar badge ---------- */

            .ax-avatar {
                width: 44px;
                height: 44px;
                min-width: 44px;
                border-radius: 50%;
                background: linear-gradient(135deg, var(--ax-primary), var(--ax-primary-dark));
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Poppins', sans-serif;
                font-weight: 700;
                font-size: 1rem;
            }

            /* ---------- Stat cards ---------- */

            .ax-stat-card {
                display: flex;
                align-items: center;
                gap: 14px;
                background-color: var(--ax-surface);
                border: 1px solid var(--ax-border);
                border-radius: var(--ax-radius-md);
                box-shadow: var(--ax-shadow);
                padding: 1.1rem 1.25rem;
                margin-bottom: 1rem;
            }

            .ax-stat-icon {
                width: 48px;
                height: 48px;
                min-width: 48px;
                border-radius: 12px;
                background-color: var(--ax-primary-light);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.4rem;
            }

            .ax-stat-value {
                font-family: 'Poppins', sans-serif;
                font-weight: 700;
                font-size: 1.5rem;
                color: var(--ax-ink);
                line-height: 1.1;
            }

            .ax-stat-label {
                font-size: 0.82rem;
                color: var(--ax-muted);
                margin-top: 2px;
            }

            /* ---------- Empty states ---------- */

            .ax-empty-state {
                text-align: center;
                padding: 1.5rem 1rem;
            }

            .ax-empty-icon {
                width: 64px;
                height: 64px;
                border-radius: 50%;
                background-color: var(--ax-primary-light);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.8rem;
                margin: 0 auto 1rem auto;
            }

            .ax-empty-state h3 {
                margin-bottom: 0.4rem !important;
            }

            .ax-empty-state p {
                max-width: 420px;
                margin: 0 auto !important;
            }
        </style>

                """
            ,unsafe_allow_html=True)
