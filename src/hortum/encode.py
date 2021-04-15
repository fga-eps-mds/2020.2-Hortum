from base64 import b64decode, b64encode

def encode_string(decoded_string):
    '''Codifica uma string pra base64'''
    b_str = decoded_string.encode('utf-8')
    b_str = b64encode(b_str)
    encoded_strings = b_str.decode('utf-8')
    return encoded_strings

def decode_string(encoded_string):
    '''Decodifica uma string em base64'''
    b_str = encoded_string.encode('utf-8')
    b_str = b64decode(b_str)
    decoded_strings = b_str.decode('utf-8')
    return decoded_strings
