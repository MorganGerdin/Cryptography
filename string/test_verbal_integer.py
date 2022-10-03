# Convert each integer part into a spoken string representation.
# Challenge: don't make an if-statement for every integer -> string case (hint: dictionary)
def integer_to_words(int_in):
    return ""


def test_integer_to_words():
    assert integer_to_words(123) == "one two three"
    assert integer_to_words(9874) == "nine eight seven four"
