# Steganography Message in Text
print("Steganography Hidden in Text Starting ...")

# Variable Declarations
# try cipherText = " act logon safe  to home bad catch or upon it!"

cipherText = input("Enter Cipher Text:")  # cipher text

numChar = len(cipherText)  # length of cipher text
curChar = 0  # current character to analyze
key = 2  # skip factor
plainText = ""  # plain text message
endpt = int(numChar / 2)

# loop that goes through all possible keys
for key in range(2, endpt):
    curChar = key - 1
    while curChar < numChar:
        plainText += cipherText[curChar]
        #skips - meat 
        curChar += key
    print("Key # " + str(key) + ": " + plainText)
    plainText = ""

print("Steganography Hidden in Text Ending ...")
