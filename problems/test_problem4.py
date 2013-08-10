from cryptotools.converters import hex_to_bytes
from cryptotools.language_score import get_top_n_meanings
from cryptotools.xor_cipher import single_char_xor_decryption_candidates


def test():
    all_candidates = (hex_to_bytes(line.strip())
                      for line in open('data/problem4_candidates.txt', 'r'))
    good_candidates = []
    for candidate in all_candidates:
        decryption_tries = single_char_xor_decryption_candidates(candidate)
        good_candidates.extend(get_top_n_meanings(decryption_tries, 1))
    good_candidates.sort(key=lambda tup: -tup[1])
    print(good_candidates[0][0])
    assert(good_candidates[0][0] == 'Now that the party is jumping\n')
