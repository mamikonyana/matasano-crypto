from utils.converters import hex_to_bytes
from utils.language_score import get_top_n_meanings
from utils.xor_cipher import single_char_xor_decryption_candidates


def test():
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bstring = hex_to_bytes(hex_string)
    candidates = single_char_xor_decryption_candidates(bstring)
    [(actual_message, score)] = get_top_n_meanings(candidates, 1)
    assert(actual_message == "Cooking MC's like a pound of bacon")
