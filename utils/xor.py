def xor_bytes(bytes1, bytes2):
    barray = bytearray([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    return bytes(barray)


def xor_with_byte(bstring, byte):
    if type(byte) == bytes:
        byte = byte[0]
    return bytes([b ^ byte for b in bstring])


def variable_length_xor(bytesting, key):
    # TODO: check that the length are multiples
    if len(bytesting) % len(key) != 0:
        same_length_string = key * (len(bytesting) // len(key) + 1)
        same_length_string = same_length_string[:len(bytesting)]
        return xor_bytes(bytesting, same_length_string)
    same_length_string = key * (len(bytesting) // len(key))
    return xor_bytes(bytesting, same_length_string)
