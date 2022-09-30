# Returns true if all elements in <potential_factors> are clean factors of <number>.
def all_factors(number, potential_factors):
    return False


def test_all_factors():
    assert all_factors(10, [2, 5])
    assert not all_factors(10, [7, 5])  # False because 7 is not a factor of 10.
