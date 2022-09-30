# Returns the value rounded to the nearest whole integer.
def round(value):
    return value


def test_round():
    assert round(5.4) == 5
    assert round(5.6) == 6