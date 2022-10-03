# You are given a collection of elements, a single <center> element, and a <check> element.
# Return the index at which a <check> element is closest to a <center> element.
# For example: given func([3, 1, 1, 2, 3], 2, 3), we are looking for the index of a <3> element closest to a <2> element
# The correct answer is 4, because the 5th element (zero-index) is 1 slot away from a 2.
# The 0th index value is also 3, but it is further away from the center 2, so "0" is an incorrect answer.

# BONUS POINTS: right now we assume there is only 1 center value.
# What if the input has multiple center and check values?
def find_closest_element(collection, center, check):
    return 0


def test_find_closest_element():
    assert find_closest_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 7], 7, 4) == 3

    # "2" element closest to a "1" element, last (7th) index is closest
    assert find_closest_element([1, 0, 0, 2, 0, 0, 1, 2], 1, 2) == 7
