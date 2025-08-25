# Transcript Assist (Dev)

## Purpose
Transcript Asisst is a lightweight internal tool to read meeting transcripts and turn them into **clear action items** (Action Item, Confirmed/Possible Status) and export them to multiple formats.
This repo is the **development version** - used to refine code, logic, and instructions before creating the packaged build ("TranscriptAssist_build) that gets shared internally.

---

## Features
- Upload a **Word (.docx)** transcript
- Clean and process transcript text
- Extra **action items** using keyword rules
- Download results as:
  - 'actions.csv' (Excel/Sharepoint)
  - 'actions.md' (Teams/email paste-ready)
  - 'actions.json' (automation/future integrations)

---

## Repository Structure
TranscriptAssist/
  - app.py # Entry point (run with Streamlit)
  - src/
    - init.py
    - main.py # Orchestrates UI and detection
    - ui.py # UI functions (upload, results, export)
    - extract.py # Parse speakers from docx
    - detect.py # Find action items with NLP
    - constants.py # Regex patterns, keywords
    - styling.py # CSS/theme loader
  - style.css # Optional extra styling
  - .streamlit/
    - config.toml # Theme + server settings
  - requirements.txt # Dependencies

  ---

## Setup (Dev)
```powershell
# 1. Clone the repo
git clone https://github.com/shalladeen-cgi/TranscriptAssist.git
cd TranscriptAssist

# 2. Create a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
---
## Run (Dev)
``` powershell
python -m streamlit run app.py
```
Then open http://localhost:8501 in your browser.
---

## Portable Build (for non-technical users)

There is also a portable version of TranscriptAssist that does not require Python.
[See Instructions and Download Link](https://groupecgi-my.sharepoint.com/:w:/g/personal/shawna_halladeen_cgi_com/EdilLJ0c1JBNpWRIbxlNzCgBrUKwBUzlkPw4augpAan5Ig?e=gItW73)

## Contributing
Keep dependencies updated in requirements.txt using:
``` powershell
pip freeze > requirements.txt
```
Always use the .venv virtual environment for local development

Run the app locally with:
``` powershell
python -m streamlit run app.py
```

