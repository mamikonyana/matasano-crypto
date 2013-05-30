from utils.converters import hex_to_bytes
from utils.language_score import get_top_n_meanings
from utils.single_char_xor_cipher import get_single_char_xor_cipher_decryptions


def test():
    all_candidates = (hex_to_bytes(line.strip())
                      for line in open('data/problem4_candidates.txt', 'r'))
    good_candidates = []
    for candidate in all_candidates:
        decryption_tries = get_single_char_xor_cipher_decryptions(candidate)
        good_candidates.extend(get_top_n_meanings(decryption_tries, 1))
    good_candidates.sort(key=lambda tup: -tup[1])
    assert(good_candidates[0][0] == 'Now that the party is jumping\n')
