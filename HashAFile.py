import hashlib

path = r'encrypted_file'

with open(path, 'rb') as opened_file:
    content = opened_file.read()
hash = hashlib.sha256(content).hexdigest()

print("Hash:", hash)