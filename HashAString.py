import hashlib

str = input("Enter a String:")
hash = hashlib.sha256(str.encode()).hexdigest()

print("Hash:", hash)