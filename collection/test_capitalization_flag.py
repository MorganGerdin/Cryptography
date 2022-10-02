# Given string <input>, return a number where each digit is 1 if the matching index string character is capital,
# or 0 for all other cases.
# Example: "Foo" results in 100, because F (capital -> 1) is followed by oo (lower-case -> 2x 0).
# Alternative example: "Hello World" results in 10000010000, because the white space is replaced by a 0.
def to_capitalization_flag(input):
    return 0


def test_to_capitalization_flag():
    assert to_capitalization_flag("ApPlE ") == 101010
