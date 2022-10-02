# Return a random decimal number between <lower> and <upper>.
# The bounds are exclusive, meaning they should never be returned from this method.
def random_in_range(lower, upper):
    return 0


def test_random_in_range():
    assert 10 < random_in_range(10, 20) < 20
    assert 5 < random_in_range(5, 120) < 120

