from wokken import st_build_online_1
from tree_utils import find_suffix_tree_arc, st_leaves_traversal


def find_substr(string: str, substr: str):
    try:
        if len(string) < len(substr):
            raise IndexError

        root = st_build_online_1(string)
        res, _, _ = find_suffix_tree_arc(string, substr, len(substr), 0, root, len(string))
        if res is not None:
            st_leaves_traversal(res)
        else:
            raise IndexError
    except IndexError:
        print("Not found")