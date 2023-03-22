# Return true if all individual numbers inside <i> are ordered from smallest to biggest.
# Example: func(1223) is true, because 1 < 2 <= 2 < 3
# Example: func(987) is false, because 9 is greater than 8

# i = [1, 2, 3]
def is_sequential_integer(i):



    # sorted(i) == list(range(min(i), max(i) + 1))
    #
    # flag = 0
    # i = 1
    # while i < len(str(i)):
    #     if (i[i] != sorted[i]):
    #         flag = 1
    #     i += 1
    #
    # # printing result
    # if (not flag):
    #     return True
    # else:
    #     return False
   # return sorted(i) == list(range(min(i), max(i)+1))
   #
   #
   # flag = 0
   # i = 1
   # while i < len(str(i)):
   #     if (i[i] < i[i - 1]):
   #         flag = 1
   #     i += 1
   #
   # # printing result
   # if (not flag):
   #     return True
   # else:
   #     return False

# print(is_sequential_integer(i))



def test_is_sequential_integer():
    assert is_sequential_integer(123456789)
    assert not is_sequential_integer(768)