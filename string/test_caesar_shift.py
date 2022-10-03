# Return a string with all characters shifted up or down in the alphabet by the amount specified in <by>.
def caesar_shift(value, by):
    return value


def test_caesar_shift():
    assert caesar_shift("abc", 1) == "bcd"
    assert caesar_shift("abc", -1) == "zab"
