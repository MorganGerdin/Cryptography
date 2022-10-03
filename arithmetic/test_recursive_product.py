# Given number <integer> and count <loops>, return the product of all numbers in the integer, repeating <loops> time.
# Example: func(555, 1) is 125, because 5 * 5 * 5 is 125.
# Example: func(555, 2) is 7, because 1 * 2 * 5 (the numbers making up the previous function result) is 10.
# Example: func(555, 3) is 0, because 1 * 0 (from func(555, 2)) is 0.
def recursively_product_elements(integer, loops):
    return 0


def test_recursively_product_elements():

    # Given <555> as input
    assert recursively_product_elements(555, 1) == 125
    assert recursively_product_elements(555, 2) == 10
    assert recursively_product_elements(555, 3) == 0

    # Given <99999> as input
    assert recursively_product_elements(99999, 1) == 59_049
    assert recursively_product_elements(99999, 2) == 0
