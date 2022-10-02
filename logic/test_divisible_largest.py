# Given integer number <num>, return True if the number is cleanly divisible by its largest digit.
# Example: is_divisible_largest_digit(123) is True, because 123 can be divided by 3.
def is_divisible_largest_digit(num):
    return False


def test_is_divisible_largest_digit():
    assert is_divisible_largest_digit(123)
    assert is_divisible_largest_digit(37303)
    assert not is_divisible_largest_digit(47)
