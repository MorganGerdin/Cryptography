# Substitution Cipher Encrypt/Decrypt
# With guidance from Sweigart, Page 209-210

print("Substituion Cipher...")
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
# KEY = 'lfwoayuisvkmnxpbdcrjtqeghz'

print("Enter Plain Text:")
message = input()
message = message.lower()
print("Enter the Substitution Key (must be 26 characters long):")
KEY = input()
cipherText = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        cipherText = cipherText + KEY[symbolIndex]
    else:
        cipherText = cipherText + symbol
print("Cipher Text: " + cipherText)
print("Substitution Cipher Ending ...")