# Given a collection of integers <values>, and 0-indexed value <n_index>, return the <n>th largest element in the list.
# Example: given a list of elements [ 1, 2, 3 ], the return value for <n:0> is 3, because 3 is the first largest element
# Passing in 2 (the third-largest element) as n would return 1.
# If the collection is empty, throw an exception.
def get_nth_largest(values, n_index):
    return 0


def test_get_nth_largest():
    # 1st largest is 4
    assert get_nth_largest([1, 2, 3, 4], 0) == 4

    # 3rd largest is 3
    assert get_nth_largest([1, 3, 4, 5], 2) == 3
