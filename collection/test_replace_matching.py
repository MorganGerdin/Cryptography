# Given target list <collection_input>, a filter list <collection_filter>, and replacement character <replacement>,
# returns a modified version of <collection_input> where all values present in <collection_filter> are replaced
# by the value defined in <replacement>.
# For example: given replace_matching([1, 2, 3], [1, 3], "a"), ["a", 2, "a"] is be returned, because "a" is
# substituted for all values present in both <collection_input> and <collection_filter>.
def replace_matching(collection_input, collection_filter, replacement):
    return None


def test_replace_matching():
    assert replace_matching([1, 2, 3, 4, 5], [1, 3], "a") == ["a", 2, "a", 4, 5]
