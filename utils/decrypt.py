from .xor_cipher import get_n_char_xor_cipher_decryptions
from .single_char_xor_cipher import get_single_char_xor_cipher_decryptions
from .language_score import get_top_n_meanings


def decrypt(bstring, n):
    parts = [None] * n
    for i in range(n):
        partial_string = bstring[i::n]
        candidates = get_single_char_xor_cipher_decryptions(partial_string)
        parts[i], score = get_top_n_meanings(candidates, 1)[0]
    return ''.join([''.join(x) for x in zip(*parts)])
