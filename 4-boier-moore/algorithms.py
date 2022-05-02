def suffix_border_array(pattern):
    pat_len = len(pattern)
    bs = [0] * pat_len

    for i in reversed(range(pat_len - 1)):
        bs_left = bs[i + 1]
        while bs_left and pattern[i] != pattern[pat_len - bs_left - 1]:
            bs_left = bs[pat_len - bs_left]
        if pattern[i] == pattern[pat_len - bs_left - 1]:
            bs[i] = bs_left + 1
        else:
            bs[i] = 0

    return bs


def bs_to_ns(bs, pat_len):
    ns = [-1] * pat_len

    for j in range(pat_len - 1):
        if bs[j] != 0:
            k = pat_len - bs[j] - 1
            ns[k] = j

    return ns


def bs_to_br(bs, pat_len):
    br = [None] * pat_len
    curr_border = bs[0]
    k = 0
    while curr_border:
        while k < pat_len - curr_border:
            br[k] = curr_border
            k += 1
        curr_border = bs[k]
    while k < pat_len:
        br[k] = 0
        k += 1

    return br


def bs_to_bsm(bs, n):
    bsm = [0] * n
    bsm[0] = bs[0]

    for i in range(n - 2, 0, -1):
        if bs[i] and bs[i] + 1 == bs[i - 1]:
            bsm[i] = bsm[n - bs[i]]
        else:
            bsm[i] = bs[i]

    return bsm
