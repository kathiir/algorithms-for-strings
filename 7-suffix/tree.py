from enum import Enum


class Node:
    def __init__(self):
        self.arcs = dict()  # This doesn't change time complexity. Python uses hash dict. Average complexity: O(1).
        self.s_ref = None
        self.arc_in = None


class Arc:
    def __init__(self):
        self.beg_idx = 0
        self.end_idx = 0
        self.dest = None
        self.dest_idx = 0
        self.src = None