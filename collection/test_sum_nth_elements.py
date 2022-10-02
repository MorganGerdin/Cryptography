# You are given collection <elements>, which is composed of integer numbers.
# Given an index factor, <n>, return the sum of all values in <elements> where their index (1-indexed) is a factor of n
def sum_nth_index_elements(elements, n):
    return 0


def test_sum_nth_index_elements():
    assert sum([1, 2, 3, 4, 5, 6], 2) == 2 * 4 * 6
    assert sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 3 * 6 * 9
