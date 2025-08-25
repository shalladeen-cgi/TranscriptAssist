from pathlib import Path
import streamlit as st

def apply(path: str | Path = None) -> None:
    if path is None:
        path = Path(__file__).resolve().parents[1] / "style.css"

    css_path = Path(path)
    if not css_path.exists():
        st.warning(f"CSS file not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")

    if hasattr(st, "html"):
        st.html(f"<style>{css}</style>")
    else:
        st.info(
            "This Streamlit version doesn’t support global CSS without unsafe. "
            "Theme from .streamlit/config.toml is applied; use a scoped component for extras."
        )
