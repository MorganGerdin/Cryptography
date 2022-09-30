# Returns a list with any element from the input collection removed if it appears more than once.
# Example: [ 1, 1, 3 ] returns [ 3 ] because 1 appears more than once.
def remove_duplicates(collection):
    return collection


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 1, 2, 3, 3, 4]) == [2, 4]
