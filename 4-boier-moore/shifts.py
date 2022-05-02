def bad_char_shift(pos_list, char_bad, pos_bad):
    if pos_bad < 0:
        return 1
    n_pos = -1
    cur_list = pos_list[char_bad]

    if cur_list is not None:
        for k in cur_list:
            if k < pos_bad:
                n_pos = k
                break

    return pos_bad - n_pos


def good_suffix_shift(nsx, br, pos_bad, pat_len):
    if pos_bad == pat_len - 1:
        return 1

    if pos_bad < 0:
        return pat_len - br[0]

    pos = nsx[pos_bad]
    if pos >= 0:
        shift = pos_bad - pos + 1
    else:
        shift = pat_len - br[pos_bad]
    return shift
