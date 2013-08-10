from cryptotools.converters import pretty_hex_str, pretty_b64_str, hex_to_bytes


def test_hextob64():
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    _bytes = hex_to_bytes(hex_string)
    b64 = pretty_b64_str(_bytes)
    assert(b64 == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    _hex = pretty_hex_str(_bytes)
    assert(_hex == hex_string)

if __name__ == '__main__':
    test_hextob64()
