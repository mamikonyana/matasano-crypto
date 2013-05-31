import re
from collections import Counter


def score_meaning(text):
    """
    Returns a score in [0,1] range if the text makes any sense in English.
    """
    all_characters = re.findall('[a-zA-Z \']', text)
    if len(all_characters) == 0:
        return 0
    repetition_count = Counter(all_characters)
    score = (len(all_characters)) ** 2 / len(repetition_count)
    all_bad_characters = re.findall('[@#$%^&*+{}[]\\|', text)
    negative_score = len(all_bad_characters)
    return score


def get_top_n_meanings(strings, n):
    """
    Returns (text, score) for top n strings
    """
    scored_strings = [(s, score_meaning(s)) for s in strings]
    scored_strings.sort(key=lambda tup: -tup[1])
    return scored_strings[:n]
