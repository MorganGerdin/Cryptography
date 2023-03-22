import rsa
import hashlib
from cryptography.fernet import Fernet

# open and read file
myfile = open("encrypted_file", "rb")
myfiledata = myfile.read()

# hash for file
hash = hashlib.sha256(myfiledata).hexdigest()

(pubkey, privkey) = rsa.newkeys(1024)

encrytpedHash = rsa.encrypt(hash.encode(), privkey)

print("the Digital Signature is:", encrytpedHash.hex())