#!/usr/bin/env python3

def to_bin(n: int, width=16):
    s = bin(n).replace("0b", "")
    return ("%0" + str(width) + "d") % int(s)


def shift_and(pattern, text):
    m = len(pattern)
    n = len(text)

    enters = []

    masks = dict()

    for j in range(m):
        masks[pattern[j]] = masks.get(pattern[j], 0) | (1 << (m - 1 - j))

    u_high = 1 << (m - 1)

    M = 0
    print(f'  {pattern}')

    for i in range(n):
        # print(f'{M >> 1 | u_high:b}:{masks[ord(text[i]) - ord(ch_beg)]:b}')
        M = (M >> 1 | u_high) & masks.get(text[i], 0)
        print(f'{text[i]} {to_bin(M, m)}')
        if M & 1:
            enters.append(i - m + 1)

    for i in enters:
        print(f'Вхождение с позиции {i}: {text[i: i + m]}')