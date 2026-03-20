import re

PROFANITY_WORDS = ["stupid", "idiot"]

# 预编译正则（只执行一次）
PROFANITY_PATTERN = re.compile(
    r'\b(' + '|'.join(PROFANITY_WORDS) + r')\b',
    re.IGNORECASE
)

def mask_match(match: re.Match) -> str:
    return '*' * len(match.group())

def mask_profanity(text: str) -> str:
    if not text:
        return ""

    return PROFANITY_PATTERN.sub(mask_match, text)