# Converts and returns the input to camelCaseFormatting.
# In camelCase, the first character is underscored, and characters after spaces
# are uppercase.
def to_camel_case(input):
    return input


def test_snake_case():
    assert to_camel_case("Hello world how are you") == "helloWorldHowAreYou"
