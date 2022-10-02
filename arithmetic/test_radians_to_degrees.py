# Given an angle in radians, return the degrees equivalent.
def radians_to_degrees(radians):
    return radians


def test_radians_to_degrees():
    # Round before comparing, because some of these numbers are irrational :)
    # You might have to tweak these unit tests if decimal precision is failing you.
    # Try rounding to 3 digits if 4 doesn't work. Resulting values were grabbed from Google and might be different
    # from what Python gives you.
    assert round(radians_to_degrees(1), 4) == 57.2958
    assert round(radians_to_degrees(0.5), 4) == 28.6479
