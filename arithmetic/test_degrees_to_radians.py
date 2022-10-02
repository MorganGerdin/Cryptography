# Given an angle in degrees, return the radian equivalent.
def degrees_to_radians(degrees):
    return degrees


def test_degrees_to_radians():
    # Round before comparing, because some of these numbers are irrational :)
    assert round(degrees_to_radians(360), 4) == 6.2832
    assert round(degrees_to_radians(180), 4) == 3.1416
