from utils.xor import variable_length_xor
from utils.language_score import score_meaning
from utils.converters import hex_to_bytes


def test():
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bstring = hex_to_bytes(hex_string)
    highest_score, actual_message = -1, None
    for i in range(256):
        b = bytes([i])
        decrypted_bytes = variable_length_xor(bstring, b)
        try:
            decrypted_string = decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            continue
        score = score_meaning(decrypted_string)
        if score > highest_score:
            highest_score, actual_message = score, decrypted_string
    assert(actual_message == "Cooking MC's like a pound of bacon")
