# Affine Cipher Encrypt/Decrypt
# Makes sure to use a prime number symbol set
# The formula is cipherText = a*plainText + b (mod 89)
# Get alphabet and Inputs from User
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=[];,._+{}|:<>? "
n = len(SYMBOLS)
a = int(input("Enter the first number of the key(a):"))
b = int(input("Enter the second number of the key(a):"))
plainText = input("Enter Plain Text:")
s = len(plainText)
cipherText = ''

# Encrypt Message Symbol by Symbol
for i in range(s):
    posPlain = SYMBOLS.find(plainText[i])
    posCipher = (posPlain * a + b) % n
    cipherText += SYMBOLS[posCipher]
print("The Cipher Text: " + cipherText)

# Compute the Decryption Key
# The formula is plainText = c * cipherText + d (mod 89)
c = 0
d = 0
for i in range(n):
    if (i * a) % n == 1:
        c = i
    d = (-1) * c * b % n
print("The Decryption Keys are: ", str(c), " & ", str(d))