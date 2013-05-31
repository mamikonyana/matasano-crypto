from .xor import variable_length_xor
from .converters import hex_to_bytes


def get_n_char_xor_cipher_decryptions(bstring, n):
    all_candidates = []
    for i in range(256 * n):
        narray = [(i >> 8 * (n - j)) % 256 for j in range(1, n+1)]
        b = bytes(narray)
        b = b'ICE'
        decrypted_bytes = variable_length_xor(bstring, b)
        try:
            decrypted_string = decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            continue
        all_candidates.append(decrypted_string)
        break
    return all_candidates
