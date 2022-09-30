from builtins import type, str


# Returns true if all elements in the collection are of 'str' type.
# Hint: check the imports in this file to figure out how to do this!
def check_all_string(collection):
    return False


def test_check_all_string():
    assert not check_all_string([1, 2, "foo"])
    assert check_all_string(["a", "b"])
