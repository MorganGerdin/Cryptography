# Converts and returns the input to kebab-case
# kebab-case-looks-like-this!
# Add dashes in place of spaces and before capital letters.
def to_kebab_case(input):
    return input


def test_pascal_case():
    assert to_kebab_case("This is KebabCase") == "this-is-kebab-case"
