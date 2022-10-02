# The input string you are given is composed of parenthesis <(, )> and characters.
# Return True if the parenthesis are appropriately nested and closed.
# example: are_scope_separators_even("(())") is true, because there are 2 closed/nested parenthesis scopes
# example 2: are_scope_separators_even("())") is false, because the ending parenthesis are not opened
def are_scope_separators_even(string):
    return False


def test_are_parenthesis_even():
    assert are_scope_separators_even("(((foo)) apple)")
    assert not are_scope_separators_even("(( banana)")
