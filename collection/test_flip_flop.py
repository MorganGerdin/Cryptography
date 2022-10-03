# Given a <collection> of elements, return a new collection with the elements reversed in order.
# Note: you're prohibited from using the .reverse() function! :D
def flip_flop(collection):
    return collection


def test_flip_flop():
    assert flip_flop([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert flip_flop(["a", "b", 5]) == [5, "b", "a"]
