# one Time Pad Encrypt
# With guidance from Sweigart, Page 318

import secrets

# Get PlainText and Key
print("Enter Plain Text:")
plainText = input().upper()
key = ''
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numPlain = len(plainText)

for i in range(numPlain):
    key += secrets.choice(SYMBOLS)
print("Random Key: ")
print(key)

# Set Up Variables
keyPos = 0  # position in the key that will be analyzed
numKey = len(key)  # length of key
numSym = len(SYMBOLS)  # number of recognized symbols
cipherText = ''  # cipher text initialized

# Encrypt
for symbol in plainText:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)  # where is the current plain text character?
        keyIndex = SYMBOLS.find(key[keyPos])  # where is the current key character?
       #meat 
        cipherIndex = symbolIndex + keyIndex  # compute cipher Index
        cipherIndex = cipherIndex % numSym
        cipherText = cipherText + SYMBOLS[cipherIndex]
    else:
        cipherText = cipherText + symbol  # no change if not in symbols
    keyPos += 1  # increment key
    keyPos = keyPos % numKey
print("Cipher Text: ")
print(cipherText)
