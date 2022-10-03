# Given size <size>, return a box made of # with a hollow center, with each side having <size> amount of # characters.
# If Python gives you trouble with the string comparison, feel free to adjust the challenge constraints.
def return_box(size):
    return "#"


def test_return_box():
    assert return_box(3) == "###" \
                            "# #" \
                            "###"

    assert return_box(4) == "####" \
                            "#  #" \
                            "#  #" \
                            "####"
