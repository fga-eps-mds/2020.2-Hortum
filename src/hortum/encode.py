from base64 import b64decode, b64encode

def encode_string(*decoded_strings):
    '''Codifica uma ou mais strings pra base64'''
    encoded_strings = []

    for string in decoded_strings:
        b_str = string.encode('utf-8')
        b_str = b64encode(b_str)
        encoded_strings.append(b_str.decode('utf-8'))

    if len(encoded_strings) > 1:
        return encoded_strings
    else:
        return encoded_strings[0]

def decode_string(*encoded_strings):
    '''Decodifica uma ou mais strings em base64'''
    decoded_strings = []

    for string in encoded_strings:
        b_str = string.encode('utf-8')
        b_str = b64decode(b_str)
        decoded_strings.append(b_str.decode('utf-8'))

    if len(decoded_strings) > 1:
        return decoded_strings
    else:
        return decoded_strings[0]
