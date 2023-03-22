# Caesar Hack
# With guidance from Sweigart, Page 54-55
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=[]\;,./!@#$%^&*()_+{}|:"<>?'
numSym = len(SYMBOLS)
print("Enter Cipher Text:")
message = input()

for key in range(numSym):
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
    print("Key # " + str(key) + ": " + translated)


