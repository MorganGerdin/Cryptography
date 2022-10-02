# Returns True if <value> is a valid smiley face.
# A smiley face is defined as a collection of characters consisting of "eyes", an optional "nose", and a "mouth."
# Eyes can be ":" or ";", nose can be "-" or "~", and smile can be "D" or ")" (feel free to tweak these rules)
# A smiley face must have eyes and a mouth, but a nose is not required.
def is_valid_smiley(value):
    return False


def test_is_valid_smiley():
    assert not is_valid_smiley(":")
    assert not is_valid_smiley(")")
    assert is_valid_smiley(":D")
    assert is_valid_smiley(";-)")
