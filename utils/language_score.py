import re
from collections import Counter


def score_meaning(text):
    """
    Returns a score in [0,1] range if the text makes any sense in English.
    """
    #all_characters = re.findall('[ -~]', text)  # match 32-126 in ASCII table
    all_characters = re.findall('[a-zA-Z ]', text)  # match 32-126 in ASCII table
    if len(all_characters) == 0:
        return 0
    repetition_count = Counter(all_characters)
    score = (len(all_characters)) ** 2 / (len(repetition_count) + len(text) / 26)
    return score


def get_top_n_meanings(strings, n):
    """
    Returns (text, score) for top n strings
    """
    scored_strings = [(s, score_meaning(s)) for s in strings]
    scored_strings.sort(key=lambda tup: -tup[1])
    return scored_strings[:n]
