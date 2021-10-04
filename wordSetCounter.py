#! /usr/bin/env python3

'''This program searches all plain text files in a folder for a word, phrase or set of words and phrases.
It prints a count of each unique item in the set, plus total types and tokens.'''

import os, re, sys

# This function prints total types, total tokens, and a count for each unique item in a list.
def typesTokensCount(myList):
    count = {} # Creates dictionary to hold the count data.

    for i in myList:
        count.setdefault(i, 0) # Creates key in dictionary for each unique item in list, with default value of 0.
        count[i] = count[i] + 1 # Adds 1 to count for each occurence of item type.

    print('Types: ' + str(len(count))) # Prints length of dictionary (e.g. number of types)
    print('Tokens: ' + str(len(myList))) # Prints length of list (e.g. number of tokens)
    print(count) # Prints dictionary (e.g. count for each type)

# Edit this regex to find relevant words and phrases. Use pipe to separate multiple items.
myRegex = re.compile(r'food security|environment|sustainability', re.I)

# Prompts user to input file path for corpus data (plain text files only).
path = input('Please enter your chosen folder with file path:\n')

# Checks that file path is valid.
while True:
    if os.path.exists(path) == True:
        break
    else:
        print('Sorry, I can\'t find this file path.')
        sys.exit()

fileList = os.listdir(path)
for file in fileList:
    if file.endswith('.txt'): # Opens and reads all files in folder with .txt extension.
        print(os.path.join(path, file)) # Prints name and location of file.
        content = open(os.path.join(path, file), 'r')
        text = content.read().lower() # Converts text to lowercase to avoid duplication in type count.
        result = myRegex.findall(text) # Creates a list of all words or phrases matching regex.
        typesTokensCount(result)

