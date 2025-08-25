import streamlit as st
from .extract import extract_speaker_blocks, extract_names
from .detect import find_action_items_with_speakers
from .ui import show_header, show_upload, show_settings_sidebar, show_results, show_export
from .styling import apply as apply_styles

def run_app():
    apply_styles()
    show_header()

    uploaded_file = show_upload()
    keywords = show_settings_sidebar()

    if uploaded_file:
        with st.spinner("Analyzing transcript…"):
            speaker_blocks = extract_speaker_blocks(uploaded_file)
            _, _first_names = extract_names(uploaded_file)
            df = find_action_items_with_speakers(speaker_blocks, keywords)

        if not df.empty:
            filtered = show_results(df)
            show_export(filtered)
        else:
            st.warning("No action items detected. Try adding broader keywords in Settings.")

