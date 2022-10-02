# Given the list of integers, <elements>, return the odd number out.
# You can assume all numbers will be the odd-one-out, or the common element.
# Example: find_unique_number([1, 1, 1, 1, 1, 2, 1, 1]) == 2, because 2 is the odd number out
def find_unique_number(elements):
    return None


def test_find_unique_number():
    assert find_unique_number([1, 1, 1, 1, 1, 2, 1, 1]) == 2
    assert find_unique_number([7, 7, 3]) == 3
