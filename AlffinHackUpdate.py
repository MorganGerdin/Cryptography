# Affine Function
# This take as inputs a message and outputs the translation
# can be used for encryption and decryption
def affine(message, a, b):
    n = len(SYMBOLS)
    s = len(message)
    translation = ''
    for i in range(s):
        posMess = SYMBOLS.find(message[i])
        posTran = (posMess * a + b) % n
        if message[i] == ' ':
            translation += ' '
        else:
            translation += SYMBOLS[posTran]
    return (translation)


# end affine

# testEnglish
def testEnglish(message):
    s = len(message)  # number of symbols in plainText
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
        testword = word.upper()
        if testword in englishWords:
            numWords += 1

    if (t > 0):
        numPerMatch = float(numWords / t) * 100

    if (letPerMatch > 85) and (numPerMatch > 35):
        print("\nWe have a possible match!")
        print("Letter Percent Match: " + str(int(letPerMatch)) + "%")
        print("Word Percent Match: " + str(int(numPerMatch)) + "%")
        return ("Match")
    else:
        return ("No Match")


# end TestEnglish Function

# Decrypting the message
def hack(cipherText):
    keysTested = 0
    startTime = time.time()
    for i in range(1, 89):
        for j in range(0, 89):
            plainText = affine(cipherText, i, j)
            # print ("i = ", i, "j = ", j)
            # print ("PlainText: ", plainText)
            test = testEnglish(plainText)
            keysTested += 1
            if (keysTested % 1000 == 0):
                print("Keys Tested: ", keysTested)
            if test == "Match":
                print("Key " + str(i) + ", " + str(j) + " found!")
                print("Plain Text Guess:", plainText)
    endTime = time.time()
    totTime = endTime - startTime
    print("This took " + str(totTime) + " seconds.")


# end hack

# mainline
import time

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=[];,._+{}|:<>?/"
print("Welcome to the Affine Cipher...")

# load dictionary
dictionaryFile = open('dictionary.txt')
englishWords = []
for word in dictionaryFile.read().split('\n'):
    englishWords.append(word)
dictionaryFile.close()
print("Dictionary Loaded...")

# calling hack
cT = input("Enter the Cipher Text:")
# cT = "L%A1 A1 | ]>1] xU ]%> Phm0 >D>dr>aoM Rdx|@o|1] 1M1]>D"
hack(cT)
print("Program Ending ... ")
exit(0)