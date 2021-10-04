#! /usr/bin/env python3

# This program searches all plain text files in a folder for a regex created from a user-inputted word or phrase.

import os, re, sys

# Prompts user to input regex.
userRegex = re.compile(input('Enter your chosen word or phrase:\n'), re.I)

# Prompts user to input file path.
path = input('Please enter your chosen folder with file path:\n')

# Checks that file path is valid.
while True:
    if os.path.exists(path) == True:
        break
    else:
        print('Sorry, I can\'t find this file path.')
        sys.exit()

# Opens and reads all files in folder with .txt extension.
# Finds and prints all instances of user's regex.
fileList = os.listdir(path)
for file in fileList:
    if file.endswith('.txt'):
        print(os.path.join(path, file))
        content = open(os.path.join(path, file), 'r+')
        text = content.read()
        result = userRegex.findall(text)
        print(result)

