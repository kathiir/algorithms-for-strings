from tree import *
from tree_utils import *


def st_build_online_1(string: str):
    n = len(string)
    tree = st_vert_init_ex(None)
    arc_0 = st_arc_init_ex(tree, string[0], 0, 0, None, 0)
    js = 0
    for i in range(1, n):
        arc_prev = None
        end_prev_idx = -1
        ref_from = None
        idx_substr = idx_arc = 0
        for j in range(js, i + 1):
            m = i - j + 1
            if j == js:
                arc_prev = arc_0
                end_prev_idx = i - 1
                idx_arc = i
                idx_substr = m - 1
            uv_arc, idx_substr, idx_arc = top_jump_bottom(string, string[j:], m, arc_prev, end_prev_idx, idx_substr, idx_arc)
            if idx_substr == m:
                js = j
                break
            arc_prev = uv_arc
            if not arc_prev:
                end_prev_idx = - 1
            elif not arc_prev.dest:
                end_prev_idx = i
            else:
                end_prev_idx = arc_prev.end_idx

            wn_node = None
            if not uv_arc:
                wn_node = tree
            else:
                wn_node = uv_arc.dest

            if uv_arc and idx_arc <= end_prev_idx:
                wn_node = st_vert_init_ex(uv_arc)
                wv_arc = st_arc_init_ex(wn_node, ord(string[idx_arc]), idx_arc, uv_arc.end_idx, uv_arc.dest, uv_arc.dest_idx)
                if uv_arc.dest:
                    uv_arc.dest.arc_in = wv_arc
                uv_arc.dest = wn_node
                uv_arc.end_idx = idx_arc - 1
                uv_arc.dest_idx = -1

                if ref_from:
                    ref_from.s_ref = wn_node
                ref_from = wn_node
            else:
                if ref_from:
                    ref_from.s_ref = wn_node
                    ref_from = None

            arc_0 = st_arc_init_ex(wn_node, ord(string[i]), i, i, None, j + 1)

    return tree
