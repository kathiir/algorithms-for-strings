from utils import *
from algorithms import *
from shifts import *


def boier_moore(pattern, text):
    alphabet = create_alphabet(text, pattern)

    pos_list = position_list(pattern, alphabet)

    pat_len = len(pattern)
    text_len = len(text)

    bs = suffix_border_array(pattern)

    br = bs_to_br(bs, pat_len)

    bs = bs_to_bsm(bs, pat_len)

    nsx = bs_to_ns(bs, pat_len)

    n_text_right = pat_len

    while n_text_right <= text_len:
        k = pat_len - 1
        i = n_text_right - 1

        while k >= 0:
            if pattern[k] != text[i]:
                break
            k -= 1
            i -= 1

        if k < 0:
            print(f'Вхождение с позиции {i + 1}:  {text[i + 1: i + 1 + pat_len]}')

        bad_rule = bad_char_shift(pos_list, text[i], k)
        good_rule = good_suffix_shift(nsx, br, k, pat_len)

        n_shift = max(bad_rule, good_rule)

        n_text_right += n_shift