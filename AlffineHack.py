
# The function has inputs a plaintext string and a list of known English words
# The function outputs a string that indicates whether the plaintext string is a match or not
import time


def testEnglish(message, englishWords):
    s = len(message)  # number of symbols in plainText
    message = message.upper()
    letPerMatch = 0.0  # letter percent match
    numPerMatch = 0.0  # word percent match
    # Part I: Compute Letter Percent Match
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numLet = 0  # number of letters in plainText
    for c in message:
        if c in letters:
            numLet += 1
    letPerMatch = float(numLet / s) * 100

    # Part II: Compute WordPercent Match
    possibleWords = message.split()
    t = 0
    numWords = 0
    for word in possibleWords:
        t += 1
        if word in englishWords:
            numWords += 1

    if (t > 0):
        numPerMatch = float(numWords / t) * 100

    if (letPerMatch > 75) and (numPerMatch > 25):
        print("\nWe have a possible match!")
        print("Letter Percent Match: " + str(int(letPerMatch)) + "%")
        print("Word Percent Match: " + str(int(numPerMatch)) + "%")
        return ("Match")
    else:
        return ("No Match")


# end TestEnglish Function

# Affine Function
# This take as inputs a plainText and a slope value and an intercept value
# The output is the cipherText
def affine(message, a, b):
    # you cannot have spaces in your alphabet
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=[];,._+{}|:<>?/'
    n = len(SYMBOLS)
    s = len(message)
    translation = ''
    for i in range(s):
        posMess = SYMBOLS.find(message[i])
        posTran = (posMess * a + b) % n
        if message[i] ==" ":
                translation = " "
        else:
            translation += SYMBOLS[posTran]
    return (translation)


# end affineEncrypt Function

# MainLine of Program
# Loading Dictionary
print("Loading Dictionary ...")
dictionaryFile = open('dictionary.txt')
englishWords = []
for word in dictionaryFile.read().split('\n'):
    englishWords.append(word)
dictionaryFile.close()

# Decrypting the message
cipherText = input("Enter cipher text: ")
keysTested = 0
startTime = time.time()
for i in range(89):
    for j in range(89):
        plainText = affine(cipherText, i, j)
        test = testEnglish(plainText, englishWords)
        keysTested += 1
        if test == "Match":
            endTime = time.time()
            totTime = endTime - startTime
            print("This took " + str(totTime) + " seconds.")
            print(str(keysTested) + " keys were tested.")
            print("\nKey " + str(i) + ", " + str(j) + " found!")
            print("Plain Text Guess: " + plainText)
            print("Program Ending ... ")
            exit(0);
exit(0)

