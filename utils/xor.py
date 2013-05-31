def xor_bytes(bytes1, bytes2):
    barray = bytearray([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    return bytes(barray)


def variable_length_xor(bytesting, key):
    # TODO: check that the length are multiples
    if len(bytesting) % len(key) != 0:
        same_length_string = key * (len(bytesting) // len(key) + 1)
        same_length_string = same_length_string[:len(bytesting)]
        return xor_bytes(bytesting, same_length_string)
    same_length_string = key * (len(bytesting) // len(key))
    return xor_bytes(bytesting, same_length_string)
