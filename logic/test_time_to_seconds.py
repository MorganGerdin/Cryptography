# Given a string in the format "hours:minutes:seconds", return the total number of seconds represented by the time.
def time_to_seconds(string):
    return 0


def test_time_to_seconds():
    assert time_to_seconds("1:00:00") == 3_600
    assert time_to_seconds("1:00:10") == 3_610
    assert time_to_seconds("2:10:00") == 7_800
