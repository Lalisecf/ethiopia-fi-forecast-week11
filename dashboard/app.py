from pathlib import Path
import streamlit as st

css_path = Path(__file__).parent / "style.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(

page_title="Financial Inclusion Dashboard",

layout="wide"

)
st.title(
"Forecasting Financial Inclusion in Ethiopia"
)
st.caption(
"10 Academy AI Mastery Week 11"
)
st.sidebar.title("Navigation")