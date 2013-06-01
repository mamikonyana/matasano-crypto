from collections import Counter


def hamming_distance(bstring1, bstring2):
    distance = 8 * abs(len(bstring1) - len(bstring2))
    for b1, b2 in zip(bstring1, bstring2):
        distance += Counter(bin(b1 ^ b2))['1']
    return distance
