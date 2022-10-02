# Given an input integer, return the product of all digits within that integer.
# Example: product_digits(123) => 6, because 1 * 2 * 3 == 6.
def product_digits(string):
    return 0


def test_product_digits():
    assert product_digits(123456789) == 362_880
    assert product_digits(54545) == 2_000
