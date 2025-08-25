import streamlit as st
from src.main import run_app

st.set_page_config(
    page_title="Transcript Action Item Extractor",
    layout="wide",
    initial_sidebar_state="expanded"
)

run_app()
