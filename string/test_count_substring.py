# Given string <base> and <substring>, return the number of times <substring> appears in <base>.
def count_substring(base, substring):
    return 0


def test_count_substring():
    assert count_substring("abcabcabc", "abc") == 3
    assert count_substring("apples", "hotdog") == 0