from typing import Iterable
import re
import pandas as pd

from .constants import ACTION_PATTERNS, ACTION_VERBS, _SOFT_CUE_RE

_nlp = None
def _nlp_en():
    global _nlp
    if _nlp is None:
        try:
            import spacy
            _nlp = spacy.load("en_core_web_sm")
        except Exception:
            _nlp = None
    return _nlp

def _is_action_item_spacy(line: str) -> bool:
    nlp = _nlp_en()
    if nlp is None:
        return False
    doc = nlp(line)
    if not doc:
        return False
    root = doc[:].root
    lemma = root.lemma_.lower()
    return (lemma in ACTION_VERBS) or (
        root.tag_ in ("MD", "VBP", "VB") and lemma in ACTION_VERBS
    )

def find_action_items_with_speakers(speaker_blocks: Iterable, keywords: Iterable[str]) -> pd.DataFrame:
    rows = []
    kw = [k.strip().lower() for k in (keywords or []) if k.strip()]

    for _, line in speaker_blocks:
        line_clean = (line or "").strip()
        if not line_clean:
            continue
        line_lower = line_clean.lower()

        keyword_match = any(k in line_lower for k in kw)
        regex_match = any(re.search(p, line_clean, re.IGNORECASE) for p in ACTION_PATTERNS)
        spacy_match = _is_action_item_spacy(line_clean)

        if keyword_match or regex_match or spacy_match:
            item_type = "Confirmed"
        else:
            has_soft_cue = bool(_SOFT_CUE_RE.search(line_clean))
            item_type = "Possible" if has_soft_cue else None

        if item_type:
            rows.append({"Action Item": line_clean, "Type": item_type})

    return pd.DataFrame(rows, columns=["Action Item", "Type"])
