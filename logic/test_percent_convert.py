# Given a string in the format <n%>, return the decimal value of that percentage.
# Example: 37% is 0.37. 250% is 2.5.
def convert_percent_string(string):
    return 0


def test_convert_percent_string():
    assert convert_percent_string("97%") == 0.97
    assert convert_percent_string("170%") == 1.7
