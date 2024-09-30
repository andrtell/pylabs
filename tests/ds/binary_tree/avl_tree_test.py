from hypothesis import given, strategies as st

import ds.list.util as util

from ds.binary_tree import AVLTree


@given(st.integers(0, 100))
def test_sorted(count):
    src = util.random_list(count, 0, 100)
    t = AVLTree()
    t.insert_from(src)
    src = list(set(src))
    src.sort()
    assert list(t) == src
