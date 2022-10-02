# Given input <string>, return True if the amount of whitespace on the left-hand side of a center character is the
# same as the amount of whitespace on the right-hand side of the same character.
# For an empty string, return False.
# Example: is_centered(" D ") is True, because the center 'D' is surrounded by an equal amount of whitespace.
def is_centered(string):
    return False


def test_is_centered():
    assert is_centered(" D ")
    assert is_centered("     X     ")
    assert not is_centered(" @     ")
