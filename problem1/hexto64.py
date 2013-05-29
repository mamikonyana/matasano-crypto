from base64 import b16encode, b16decode, b64encode, b64decode


def pretty_b64_str(_bytes):
    return str(b64encode(_bytes), 'utf-8')


def pretty_hex_str(_bytes):
    return str(b16encode(_bytes), 'utf-8').lower()


def hex_to_bytes(hex_str):
    return b16decode(hex_str.upper())


def b64_to_bytes(b64_str):
    return b64decode(b64_str)


