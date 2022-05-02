from tree import Arc, Node


def st_vert_init_ex(arc_in: Arc):
    vert = Node(128)
    vert.arc_in = arc_in
    return vert


def st_arc_init_ex(s_node: Node, ch_arc_idx, beg_idx, end_idx, dest: Node, dest_idx):
    arc = Arc()
    arc.beg_idx = beg_idx
    arc.end_idx = end_idx
    s_node.arcs[ch_arc_idx] = arc
    arc.dest = dest
    arc.dest_idx = dest_idx
    arc.src = s_node
    return arc


def find_suffix_tree_arc(string: str, substring: str, m: int, m_same: int, tree: Node):
    arc = None
    idx_substr = idx_arc = 0
    cur = tree
    stopped = False
    while not stopped and cur:
        next_arc = cur.arcs[substring[idx_substr]]
        if next_arc:
            arc = next_arc
            idx_arc = arc.beg_idx
            n_same_rest = m_same - idx_substr
            if n_same_rest > 0:
                n_arc_len = arc.end_idx - arc.beg_idx + 1
                if n_same_rest <= n_arc_len:
                    idx_substr = m_same - 1
                    idx_arc += n_same_rest - 1
                else:
                    idx_substr += n_arc_len
                    idx_arc = arc.end_idx + 1
                    cur = arc.dest
                    continue
            while idx_substr < m and idx_arc < arc.end_idx + 1 and substring[idx_substr] == string[idx_arc]:
                idx_substr += 1
                idx_arc += 1
            if idx_arc <= arc.end_idx:
                stopped = True
            else:
                cur = arc.dest
        else:
            stopped = True
    if idx_substr == m:
        idx_arc += 1
    return arc, idx_substr, idx_arc


def st_leaves_traversal(start: Arc, n_alpha):
    if start.dest_idx >= 0:
        print(f'Position found: {start.dest_idx}')
    else:
        start = start.dest
        for k in range(n_alpha):
            arc = start.arcs[k]
            if arc:
                st_leaves_traversal(arc, n_alpha)


def top_jump_bottom(string: str, substring: str, m: int, arc: Arc, arc_end_idx: int, idx_substr: int, idx_arc: int):
    if not arc:
        return None
    arc_next = None
    src_vert = None
    is_inner_vert = arc.dest and (idx_arc > arc_end_idx)
    if is_inner_vert:
        src_vert = arc.dest
    else:
        src_vert = arc.src
    ref_vert = src_vert.s_ref
    if not ref_vert:
        ref_vert = src_vert
    n_chars_up = 1 if is_inner_vert else idx_arc - arc.beg_idx + 1
    if not src_vert.s_ref:
        n_chars_up -= 1
    n_vert_chr = m - n_chars_up
    arc_next, idx_substr, idx_arc = find_suffix_tree_arc(string, substring[n_vert_chr:], n_chars_up, n_chars_up - 1, ref_vert)
    if not arc_next:
        arc_next = ref_vert.arc_in
        if arc_next:
            idx_arc = arc_next.end_idx + 1
    idx_substr += n_vert_chr
    return arc_next, idx_substr, idx_arc

