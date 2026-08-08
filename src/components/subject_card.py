import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:var(--ax-surface); border-left: 6px solid var(--ax-primary); padding:22px 26px; border-radius: var(--ax-radius-md); box-shadow: var(--ax-shadow); margin-bottom:18px;">
        <h3 style="margin:0; color: var(--ax-ink); font-size: 1.3rem;">{name}</h3>
        <p style="color:var(--ax-muted); margin:8px 0 14px 0; font-size:.92rem;">Code&nbsp;
            <span style="background:var(--ax-primary-light); color:var(--ax-primary); padding:2px 10px; border-radius:8px; font-weight:600;">{code}</span>
            &nbsp;&middot;&nbsp;Section {section}
        </p>

        """

    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: var(--ax-primary-light); padding:5px 12px; border-radius:10px; font-size:0.85rem; color:var(--ax-ink);">{icon} <b>{value}</b> {label}</div>'

        html+= "</div>"
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
