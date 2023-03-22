# Substitution Hack
# With guidance from Sweigart, Page 209-210

print("Substitution Hack Beginning...")
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
cipherText = input("ciphertext:")
cipherText = cipherText.lower()
# print("Cipher Text: \n" + cipherText)

# initialize letterCount List
letterCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(str(letterCount))

for letter in cipherText:
    if letter in SYMBOLS:
        pos = SYMBOLS.find(letter)
        letterCount[pos] += 1

print("\nLetter Analysis")
print(str(letterCount))
# the code in between could take days
print("Enter the Substitution Key (must be 26 characters long):")
KEY = input()
plainText = ''

for symbol in cipherText:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        plainText = plainText + KEY[symbolIndex]
    else:
        plainText = plainText + symbol
print("Plain Text: " + plainText)
print("Substitution Hack Ending ...")


