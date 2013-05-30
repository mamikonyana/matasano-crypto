from problem2 import xor_bytes


def variable_length_xor(bytesting, key):
    # TODO: check that the length are multiples
    if len(bytesting) % len(key) != 0:
        raise Exception()
    same_length_string = key * (len(bytesting) // len(key))
    return xor_bytes(bytesting, same_length_string)
