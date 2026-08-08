import streamlit as st


def stat_row(items):
    """items: list of (icon, label, value) tuples, rendered as equal-width KPI cards."""
    cols = st.columns(len(items))

    for col, (icon, label, value) in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="ax-stat-card">
                    <div class="ax-stat-icon">{icon}</div>
                    <div>
                        <div class="ax-stat-value">{value}</div>
                        <div class="ax-stat-label">{label}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
