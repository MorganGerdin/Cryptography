# Converts and returns the input to PascalCase.
# In PascalCase, the first character & characters after spaces are upper-cased.
# All other characters are lower-cased. Spaces are removed.
def to_pascal_case(input):
    return input


def test_pascal_case():
    assert to_pascal_case("this is pascal case") == "ThisIsPascalCase"
