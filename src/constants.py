import re

# Regex patterns
SPEAKER_LINE_PATTERN = re.compile(
    r"""^
        (?P<speaker>[A-Za-z][\w'.-]+,\s+[A-Za-z][\w'.-]+)   # Last, First
        (?:\s{2,}|\t)+                                      # gap (spaces/tabs)
        (?:\d{1,2}:\d{2}:\d{2})?                            # optional HH:MM:SS
        (?:\s+(?P<speech>.+))?                              # optional inline speech
        \s*$
    """,
    re.VERBOSE
)

INLINE_SPEAKER_SAY_PATTERN = re.compile(
    r"""^
        (?P<speaker>[A-Za-z][\w'.-]+,\s+[A-Za-z][\w'.-]+)
        \s*[:\-–—]\s*
        (?P<speech>.+)
        $
    """,
    re.VERBOSE
)

NAME_CAPTURE_PATTERN = re.compile(
    r"\b([A-Z][a-z]+,\s[A-Z][a-z]+(?:\s[A-Z]\.)?)\b"
)

# Action trigger patterns (regex)
ACTION_PATTERNS = [
    r"\b(can you|please|make sure|follow up|remind|send|complete|schedule|"
    r"take care of|ensure|need to|have to|required to|I'll|I will|let's|should)\b.*",
]

# Token lemmas that strongly indicate actions
ACTION_VERBS = {
    "share", "talk", "assign", "send", "remind", "follow", "check",
    "email", "connect", "complete", "submit", "update"
}

# Default keyword seed (comma-separated input will be split in UI)
DEFAULT_KEYWORDS = (
    "action, follow up, send, complete, email, share, remind, assign, connect, confirm"
)
