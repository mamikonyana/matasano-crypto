from utils.encrypt import hex_xor_encrypt
from utils.converters import hex_to_bytes
from utils.decrypt import decrypt


def test():
    string = '''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
    key = "ICE"
    assert(hex_xor_encrypt(string, key) == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')


def test_reverse():
    string = '''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
    hex_string = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    bstring = hex_to_bytes(hex_string)
    assert(decrypt(bstring, 3) == string)
