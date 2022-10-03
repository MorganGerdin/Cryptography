# Given a collection of numbers, return a collection of the same size consisting of the square of each element.
# Example: func([1, 2, 3]) is [1, 4, 9], because each element is squared and present at the same index.
# BONUS CHALLENGE: add an argument to specify the power each number is raised to!
def to_power_collection(numbers):
    return numbers


def test_to_power_collection():
    assert to_power_collection([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
