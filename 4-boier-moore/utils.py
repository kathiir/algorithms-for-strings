def create_alphabet(text, pattern):
    alphabet = ''
    for char in text:
        if char not in alphabet:
            alphabet += char
    for char in pattern:
        if char not in alphabet:
            alphabet += char
    return alphabet


def position_list(string, alphabet):
    m_string = len(string)

    pos_list = {}

    for ch in alphabet:
        pos_list[ch] = []

    for k in reversed(range(0, m_string)):
        index_char = string[k]

        pos_list[index_char].append(k)

    return pos_list
