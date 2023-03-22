# Detect English module
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# To use, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # Returns True or False
# (There must be a "dictionary.txt" file in this directory with all
# English words in it, one word per line. You can download this from
# https://www.nostarch.com/crackingcodes/.)


UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
        dictionaryFile.close()
    return englishWords


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0  # No words at all, so return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=10, letterPercentage=95):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spacesa, s
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    # return boolan values - both must be true
  #  print (getEnglishCount(message))
    #print(wordsMatch, lettersMatch)
    return wordsMatch and lettersMatch
    # take out one and two letter words then test



# mainline
ENGLISH_WORDS = loadDictionary()
plaintext = input("Plaintext:")
Percent = str(round(getEnglishCount(plaintext), 2))
Test = str((isEnglish(plaintext)))

print("The percent of English words in the text is: " + Percent + "%")

if Test == "True":
    print("The text is English")

elif Test == "False":
    print("The test is not English")

else:
    print("An error has occurred")





