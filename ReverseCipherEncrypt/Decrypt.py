# This is the Reverse Cipher
# Made by Jon Zderad on 8/15/2020
# With guidance from Sweigart, Page 40
print("Enter Plain Text:")
message = input()
translated = ''
i = len(message) - 1
print("Your message has " + str(i) + " characters.")
while i>=0:
    translated = translated + message[i]
    i -= 1
print("The Cipher Text is: " + translated)