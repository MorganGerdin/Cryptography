# You must evaluate the "passion level" of the input string, which is a numerical rating of how passionate
# the person posting it is. The rules are as follows:
# >50% capital letters is 1 point
# 1 or more exclamation point is 1 point
# 5 or more exclamation points is an additional 1 point
# All rules can be combined for a maximum of up to 3 points
# BONUS CHALLENGE: any input string ending with "..." gains minus 1 point
def get_passion_level(check):
    return 0


def test_passion_level():
    assert get_passion_level("woohoo") == 0
    assert get_passion_level("Woohoo") == 0
    assert get_passion_level("WOOHOO") == 1
    assert get_passion_level("woohoo!") == 1
    assert get_passion_level("WOOHOO!") == 2
    assert get_passion_level("WOOHOO!!!!!") == 3
    assert get_passion_level("woohoo...") == -1
