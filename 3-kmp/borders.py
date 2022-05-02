def prefix_border_array(string: str):
    bp = [0]
    for i in range(1, len(string)):  # длина префикса
        right = bp[i - 1]  # Позиция справа от предыдущей грани
        while right and string[i] != string[right]:
            right = bp[right - 1]
        if string[i] == string[right]:
            bp.append(right + 1)  # Длина на 1 больше, чем позиция
        else:
            bp.append(0)
    return bp


def prefix_border_array_mod(string, bp):
    bpm = [0] * len(bp)
    bpm[0] = 0
    n = len(string)
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):
        if bp[i] and (string[bp[i]] == string[i + 1]):
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    return bpm


def bp_to_bpm(bp, n):
    bpm = [0] * n
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):
        if bp[i] and bp[i] + 1 == bp[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    return bpm


def suffix_border_array(string):
    n = len(string)
    bs = [0] * n
    for i in reversed(range(n - 1)):
        left = bs[i + 1]
        while left and string[i] != string[n - left - 1]:
            left = bs[n - left]
        if string[i] == string[n - left - 1]:
            bs[i] = left + 1
        else:
            bs[i] = 0
    return bs


def bs_to_bsm(bs, n):
    bsm = [0] * n
    bsm[0] = bs[0]

    for i in range(n - 2, 0, -1):
        if bs[i] and bs[i] + 1 == bs[i - 1]:
            bsm[i] = bsm[n - bs[i]]
        else:
            bsm[i] = bs[i]

    return bsm