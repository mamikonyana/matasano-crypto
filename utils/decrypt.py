from .xor_cipher import get_n_char_xor_cipher_decryptions
from .language_score import get_top_n_meanings


def decrypt(bstring, n_range):
    for n in n_range:
        candidates = get_n_char_xor_cipher_decryptions(bstring, n)
        message, score = get_top_n_meanings(candidates, 1)[0]
        return message
