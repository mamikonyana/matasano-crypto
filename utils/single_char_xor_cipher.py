from .xor import variable_length_xor


def get_single_char_xor_cipher_decryptions(bstring):
    all_candidates = []
    for i in range(256):
        b = bytes([i])
        decrypted_bytes = variable_length_xor(bstring, b)
        try:
            decrypted_string = decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            continue
        all_candidates.append(decrypted_string)
    return all_candidates
