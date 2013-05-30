from utils.converters import hex_to_bytes, pretty_hex_str
from utils.xor import xor_bytes


def test_xor():
    hex1 = '1c0111001f010100061a024b53535009181c'
    hex2 = '686974207468652062756c6c277320657965'
    b1, b2 = hex_to_bytes(hex1), hex_to_bytes(hex2)
    b3 = xor_bytes(b1, b2)
    assert(pretty_hex_str(b3) == '746865206b696420646f6e277420706c6179')
