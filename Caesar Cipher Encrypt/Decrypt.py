# Ceasar Cipher Encrypt
# With guidance from Sweigart, Page 54-55
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=[]\;,./!@#$%^&*()_+{}|:"<>?'
numSym = len(SYMBOLS)
print (numSym)
print("Enter Plain Text:")
message = input()
print("Enter the Key:")
key = input()
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex + int(key)
        if translatedIndex >= numSym:
            translatedIndex -= numSym
        elif translatedIndex < 0:
            translatedIndex += numSym
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print("Cipher Text: "+translated)