from .xor import variable_length_xor
from .converters import pretty_hex_str


def hex_xor_encrypt(string, key):
    bstring = string.encode('utf-8')
    bkey = key.encode('utf-8')
    encryption = variable_length_xor(bstring, bkey)
    return pretty_hex_str(encryption)
