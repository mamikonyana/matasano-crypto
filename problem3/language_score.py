import re
from collections import Counter


def score_meaning(text):
    """
    Returns a score in [0,1] range if the text makes any sense in English.
    """
    all_characters = re.findall('[a-zA-Z]', text)
    if len(all_characters) == 0:
        return 0
    repetition_count = Counter(all_characters)
    return (len(all_characters)) ** 2 / len(repetition_count)