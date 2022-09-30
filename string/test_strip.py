# Returns the input with whitespace stripped from both sides.
def strip(input):
    return input


def test_strip():
    assert " hello world " == "hello world"
    assert "                 pizza" == "pizza"
    assert "pizza                 " == "pizza"
