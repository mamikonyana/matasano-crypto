def xor_bytes(bytes1, bytes2):
    barray = bytearray([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    return bytes(barray)
