# Given an input collection of strings that can be parsed as integers, returns the resulting sum of all input values
# when converted to an integer, as a string.
def add_string_numbers(collection):
    return ""


def test_add_string_numbers():
    assert add_string_numbers(["1", "2"]) == "3"
    assert add_string_numbers(["100", "200", "50"]) == "350"
