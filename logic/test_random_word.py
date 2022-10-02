# Given string <sentence>, return a random word from that sentence.
# You can remove punctuation and capitalization when processing the sentence.
def get_random_word(sentence):
    return sentence


def test_random_word():
    assert get_random_word("Hello, world! I love pizza!") in ["hello", "world", "i", "love", "pizza"]
