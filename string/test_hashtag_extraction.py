# You are a developer at a social media company, and you need to process messages for hashtags.
# Return a collection of all hashtags found within the provided message.
# A hashtag is defined as a group of characters that starts with # and is ended by a whitespace.
# Ignore special characters (!, ,, ., ?,, etc.) when processing hashtags
def extract_hashtags(message):
    return []


def test_extract_hashtags():
    assert extract_hashtags("Hello #everybody, I love eating #pizza! #goals") == [ "everybody", "pizza", "goals"]
