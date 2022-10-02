# Create and return a Christmas Tree out of # characters, based off the number of levels specified.
# christmas_tree(3) will return:
#            __#__
#            _###_
#            #####
# (without the underscores, which represent white space)
def christmas_tree(levels):
    return "#"


def test_christmas_tree():
    assert christmas_tree(3) == ("  #  "
                                 " ### "
                                 "#####")
