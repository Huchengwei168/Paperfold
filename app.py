"""Launch the paper model workbench in Streamlit."""

from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"

st.set_page_config(
    page_title="纸模工坊",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html("""
<style>
[data-testid="stHeader"] { display: none; }
[data-testid="stMainBlockContainer"] { max-width: none; padding: 0; }
[data-testid="stMainBlockContainer"] iframe { height: 100dvh !important; }
</style>
""")

page = (WEB / "index.html").read_text(encoding="utf-8")
script = (WEB / "app.js").read_text(encoding="utf-8")
# Load the checked-in JavaScript inside the frame. Imported pictures stay in the browser.
page = page.replace('<script src="app.js"></script>', f"<script>\n{script}\n</script>")
st.iframe(page, height=850, width="stretch")
