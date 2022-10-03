# Given a Collection of Boolean values, return the number of True values that occur in the longest consecutive sequence
# of True values.
# Example: func([T, F, T, T]) is 2, because the longest sequence of True is [ T, T ] at the end of the input array.
def count_longest_sequence(booleans):
    return 0


def test_count_longest_sequence():
    assert count_longest_sequence([True, True, True, True, False, True, True]) == 4
