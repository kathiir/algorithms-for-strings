from wokken import st_build_online_1
from tree_utils import st_leaves_traversal, find_suffix_tree_arc


def find_substr(string: str, substr: str):
    root = st_build_online_1(string)
    res, _, _ = find_suffix_tree_arc(string, substr, len(substr), -1, root)
    if res is not None:
        st_leaves_traversal(res)
    else:
        print("Not found")


if __name__ == "__main__":
    find_substr("abracadabra", "abrac")