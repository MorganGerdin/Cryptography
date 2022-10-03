# Zipper merge collections <a> and <b>, and assume they are the same length / non-empty. Start with <a>.
def zipper_merge(a, b):
    return a


def test_zipper_merge():
    assert zipper_merge(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
