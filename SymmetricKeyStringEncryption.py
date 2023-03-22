from cryptography.fernet import Fernet

receiver = input ("Please log into the network")

if receiver != "Bob":

     print ("Error logging into network")

     exit ()

assignment = input("Hello Bob, would you'd like to send a key to Alice (send) or decrypt?")
if assignment == "send":
    key = Fernet.generate_key()

print ("Your key has been sent.")

sender = input("Please log into the network")

if sender != "Alice":

   print ("Error logging into network")

   exit()

print ("Bob the secret key is :", key)

print ("Make sure no one else knows")
message = input("Message:").encode()


cipher = Fernet(key)

encryptedText = cipher.encrypt(message)

print("The encrypted message is :", encryptedText)

print("Encrypted Message has been sent.")

receiver = input ("Please log into the network:")

if receiver != "Bob":

   print("Error logging into network")

   exit()

originalText = cipher.decrypt(encryptedText)

print("Plain Text is: ", originalText)

print("Logging Out")

key = Fernet.generate_key()

print("The Key is : ")

cipher = Fernet(key)

encrypted_text = cipher.encrypt(b"this is my secret message")

print (encrypted_text)

original_text = cipher.decrypt(encrypted_text)

print(original_text)

