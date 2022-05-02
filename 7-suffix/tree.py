
class Node:
    def __init__(self, n_alpha):
        self.arcs = [None] * n_alpha
        self.s_ref = None
        self.arc_in = None


class Arc:
    def __init__(self):
        self.beg_idx = 0
        self.end_idx = 0
        self.dest = None
        self.dest_idx = 0
        self.src = None

