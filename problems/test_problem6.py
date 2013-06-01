from utils.converters import b64_to_bytes
from utils.hamming_distance import hamming_distance
from utils.decrypt import decrypt


def test():
    raw_bytes = b''.join([b64_to_bytes(line.strip()) for line in
                          open('data/problem6_b64_strings.txt', 'r')])
    assert(hamming_distance('this is a test'.encode('utf-8'),
                            'wokka wokka!!!'.encode('utf-8')) == 37)

    def norm_ham_dist(keysize):
        return hamming_distance(raw_bytes[:keysize], raw_bytes[keysize:2 * keysize]) / keysize

    keysize = min(range(2, 40), key=norm_ham_dist)
    print('keysize', keysize)
    print(decrypt(raw_bytes, keysize))
