import streamlit as st
import pandas as pd
from .constants import DEFAULT_KEYWORDS

def show_header():
    left, right = st.columns([0.8, 0.2])
    with left:
        st.title("Extract Action Items From Your Transcript")
        st.info("Upload a .docx transcript and extract action items with speaker attribution.")

        st.empty()
    st.divider()

def show_upload():
    st.subheader("Upload Your File")
    return st.file_uploader("Choose a Word document (.docx)", type=["docx"])

def show_settings_sidebar():
    st.sidebar.title("Settings")
    use_custom = st.sidebar.checkbox(
        "Customize keywords",
        key="use_custom",
        help="Optional. Defaults are safe and conservative. Keep terms broad."
    )

    if use_custom:
        kw_text = st.sidebar.text_area(
            "Comma-separated keywords",
            value=st.session_state.get("kw_text", DEFAULT_KEYWORDS),
            height=250,
            key="kw_text_area",
        )
        st.session_state.kw_text = kw_text
        kws = [k.strip() for k in kw_text.split(",") if k.strip()]
        if len(kws) < 3:
            st.sidebar.info("Using defaults (need at least 3 keywords).")
            kws = [k.strip() for k in DEFAULT_KEYWORDS.split(",") if k.strip()]
    else:
        kws = [k.strip() for k in DEFAULT_KEYWORDS.split(",") if k.strip()]

    return kws

def show_results(df: pd.DataFrame):
    total = len(df)
    confirmed = int((df["Type"] == "Confirmed").sum()) if total else 0
    possible = total - confirmed

    st.subheader("Results")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", total)
    c2.metric("Confirmed", confirmed)
    c3.metric("Possible", possible)

    with st.expander("Filters", expanded=False):
        _df = df.copy()
        if "Speaker" in _df.columns:
            speakers = sorted([s for s in _df["Speaker"].dropna().unique()])
            if speakers:
                sel_speakers = st.multiselect("Speaker", speakers, default=speakers)
                _df = _df[_df["Speaker"].isin(sel_speakers)]
        types = sorted([t for t in _df["Type"].dropna().unique()]) if not _df.empty else []
        if types:
            sel_types = st.multiselect("Type", types, default=types)
            if sel_types:
                _df = _df[_df["Type"].isin(sel_types)]
        q = st.text_input("Search text", placeholder="Find anything…")
        if q:
            _df = _df[_df["Action Item"].str.contains(q, case=False, na=False)]

    st.dataframe(_df, height=380, use_container_width=True)
    return _df

def show_export(df: pd.DataFrame):
    st.subheader("Export")
    col1, col2, col3 = st.columns(3)
    with col1:
        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv_data, "action_items.csv", "text/csv")
    with col2:
        json_data = df.to_json(orient="records", indent=4)
        st.download_button("Download JSON", json_data, "action_items.json", "application/json")
    with col3:
        md_output = "\n".join(
            f"- **{row.get('Action Item','')}** _(Type: {row.get('Type','')}; Speaker: {row.get('Speaker','N/A')})_"
            for _, row in df.iterrows()
        )
        st.download_button("Download Markdown", md_output, "action_items.md", "text/markdown")
