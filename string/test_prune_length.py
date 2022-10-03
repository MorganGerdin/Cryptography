# Given <string> and <max_length>, return a string with 3 periods taking the place of any trailing characters
# after the max length in the input string.
# Example: func("Hello", 3") is "Hel...", because Hello is longer than 3 characters
# Example 2: func("foo", 5) is still "foo", because it was not trimmed by the max length
# Example 3: func("pizza is super awesome", 1) is "p..."
def prune_ending(string, max_length):
    return string


def test_prune_ending():
    assert prune_ending("123456789", 7) == "1234567..."
    assert prune_ending("hello world", 5) == "hello..."
    assert prune_ending("hello", 5) == "hello"
