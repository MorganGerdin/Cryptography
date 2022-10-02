# Given string <string>, return an integer composed of all digits in the input string.
# For example, extract_digits("foo123apple1") => 1231, because 1231 is composed of all integers in the input string.
def extract_digits(string):
    return 0


def test_extract_digits():
    assert extract_digits("123abc456") == 123456
