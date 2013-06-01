from .language_score import get_top_n_meanings
from .xor_cipher import single_char_xor_decryption_candidates


def decrypt(bstring, n):
    parts = [None] * n
    for i in range(n):
        partial_string = bstring[i::n]
        candidates = single_char_xor_decryption_candidates(partial_string)
        parts[i], score = get_top_n_meanings(candidates, 1)[0]

    main = ''.join([''.join(x) for x in zip(*parts)])
    last_part_length = len(parts[-1])
    ending = ''.join([x for part in parts
                      for rest in part[last_part_length:]
                      for x in rest])
    return main + ending
