import streamlit as st


def empty_state(icon, title, message, key, cta_label=None):
    """Friendly placeholder for empty lists/tables. Returns True if the optional CTA was clicked."""
    clicked = False

    with st.container(border=True, key=f"ax_card_empty_{key}"):
        st.markdown(
            f"""
            <div class="ax-empty-state">
                <div class="ax-empty-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if cta_label:
            _, mid, _ = st.columns([1, 1.4, 1])
            with mid:
                clicked = st.button(cta_label, type='primary', width='stretch', key=f"ax_empty_cta_{key}")

    return clicked
