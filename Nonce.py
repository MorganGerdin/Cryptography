import hashlib

# mainline
# input message
message = input("Enter your message")

# get hash for message
print("This is the hash without a nonce ...")
message_hash = hashlib.sha256(message.encode()).hexdigest()
print(message_hash)

# find a nonce
for x in range(10000, 99999):
    message_with_nonce = message + str(x)
    message_with_nonce_hash = hashlib.sha256(message_with_nonce.encode()).hexdigest()
    if ((message_with_nonce_hash[0] == '0') and (message_with_nonce_hash[1] == '0')
            and (message_with_nonce_hash[2] == '0') and (message_with_nonce_hash[3] == '0')):
        print("The nonce is :", x)
        break

# send message with nonce and hash
print("The message with nonce is : ", message_with_nonce)
print("The hash with nonce is :", message_with_nonce_hash)
exit(0)