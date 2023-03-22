# You are a developer at a social media company, and you need to process messages for hashtags.
# Return a collection of all hashtags found within the provided message.
# A hashtag is defined as a group of characters that starts with # and is ended by a whitespace.
# Ignore special characters (!, ,, ., ?,, etc.) when processing hashtags
def extract_hashtags(message):
    message = message.split(" ")
    count = 0
    hashList = []
    for item in message:
        for char in item:
            count += 1
            if char == "#":
                flag = True
            else:
                flag = False

            if flag:
                hashList.append(item)

    hashList = [ele.replace("#", '').replace("!", "").replace(",", "").replace(".", "").replace("?", "") for ele in
                hashList]

    return hashList


def test_extract_hashtags():
    assert extract_hashtags("Hello #everybody, I love eating #pizza! #goals") == [ "everybody", "pizza", "goals"]


def test2_extract_hashtags():
    assert extract_hashtags("#Hello peoples, #loveEating #iceCreaM!!!") == ["Hello", "loveEating", "iceCreaM"]
    assert not extract_hashtags("#IDK") == ["#IDK"]








