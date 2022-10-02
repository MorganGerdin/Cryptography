# Return true if <number> is a power of <number>.
# Example: is_power(16, 2) is True, because 2^4 is 16.
# is_power(12, 4) is False, because given 4^n, where n is a whole number, it cannot equal 12.
# NOTE: you can't always return true for clean division, because while 7 goes into 14, it is not a power factor.
def is_power(number, power):
    return False


def test_is_power():
    assert is_power(16, 2)
    assert is_power(2187, 3)
    assert not is_power(4, 12)
