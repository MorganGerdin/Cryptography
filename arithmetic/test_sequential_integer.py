# Return true if all individual numbers inside <i> are ordered from smallest to biggest.
# Example: func(1223) is true, because 1 < 2 <= 2 < 3
# Example: func(987) is false, because 9 is greater than 8

def is_sequential_integer(i):
    i = str(i)
    k = []
    for item in i:
        k.append(item)
    new = sorted(k)
    if k == new:
        return True
    else:
        return False

def test_is_sequential_integer():
    assert is_sequential_integer(123456789)
    assert not is_sequential_integer(768)

def test2_is_sequential_integer():
    assert is_sequential_integer(000)
    assert not is_sequential_integer(32557554637547326)


def test3_is_sequential_integer():
    assert not is_sequential_integer(8765431)
    assert is_sequential_integer(178)
