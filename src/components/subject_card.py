import streamlit as st

ACCENTS = [
    ("#4F46E5", "#EEF2FF"),  # indigo
    ("#0D9488", "#F0FDFA"),  # teal
    ("#D97706", "#FFFBEB"),  # amber
]


def subject_card(name, code, section, stats=None, footer_callback=None, accent_index=0, progress=None):
    color, tint = ACCENTS[accent_index % len(ACCENTS)]
    initial = (name[:1] or "?").upper()

    html = f"""
        <div style="background:var(--ax-surface); border-left: 6px solid {color}; padding:22px 26px; border-radius: var(--ax-radius-md); box-shadow: var(--ax-shadow); margin-bottom:18px;">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:4px;">
            <div style="width:44px; height:44px; min-width:44px; border-radius:12px; background:{tint}; color:{color}; display:flex; align-items:center; justify-content:center; font-family:'Poppins',sans-serif; font-weight:700; font-size:1.1rem;">{initial}</div>
            <div>
                <h3 style="margin:0; color: var(--ax-ink); font-size: 1.3rem;">{name}</h3>
                <p style="color:var(--ax-muted); margin:4px 0 0 0; font-size:.9rem;">Code&nbsp;
                    <span style="background:{tint}; color:{color}; padding:2px 10px; border-radius:8px; font-weight:600;">{code}</span>
                    &nbsp;&middot;&nbsp;Section {section}
                </p>
            </div>
        </div>
        <div style="margin-top:16px;">
        """

    if stats:
        html += '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += f'<div style="background: {tint}; padding:5px 12px; border-radius:10px; font-size:0.85rem; color:var(--ax-ink);">{icon} <b>{value}</b> {label}</div>'
        html += "</div>"

    if progress is not None:
        pct = max(0, min(100, progress))
        html += f"""
        <div style="margin-top:14px;">
            <div style="height:8px; background:{tint}; border-radius:6px; overflow:hidden;">
                <div style="height:100%; width:{pct}%; background:{color}; border-radius:6px;"></div>
            </div>
            <p style="margin:6px 0 0 0; font-size:.78rem; color:var(--ax-muted);">{pct:.0f}% attendance</p>
        </div>
        """

    html += "</div></div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
