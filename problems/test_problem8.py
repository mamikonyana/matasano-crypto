import requests

from collections import Counter
from cryptotools.converters import hex_to_bytes
from cryptotools.cipher.block import blockify


def test_detect():
    response = requests.get('https://gist.github.com/tqbf/3132928/raw/6f74d4131d02dee3dd0766bd99a6b46c965491cc/gistfile1.txt')
    hex_text = response.content.decode('utf-8')
    cipher, index, max_repeatitions = None, None, 0
    for indx, candidate in enumerate(hex_text.split('\n')):
        if not candidate:
            continue
        ciphertext = hex_to_bytes(candidate)
        [(block, count)] = Counter(blockify(ciphertext, 16)).most_common(1)
        if count > max_repeatitions:
            cipher = candidate
            index = indx
            max_repeatitions = count
    assert index == 132
    assert max_repeatitions == 4
    assert cipher == 'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a'
