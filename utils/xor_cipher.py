from .xor import xor_with_byte


def single_char_xor_decryption_candidates(bstring):
    all_candidates = []
    for i in range(256):
        decrypted_bytes = xor_with_byte(bstring, i)
        try:
            decrypted_string = decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            continue
        all_candidates.append(decrypted_string)
    return all_candidates
