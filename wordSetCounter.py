#! /usr/bin/env python3

'''This program searches all plain text files in a folder for a word, phrase or set of words and phrases.
It generates a count of each unique item in the set, plus total types and tokens.
Results are saved to a file.'''

from pathlib import Path
import os, re, sys, json

# This function appends to resultsFile the total types, total tokens, and a count for each unique item in a list.
def typesTokensCount(myList):
    
    count = {} # Creates dictionary to hold the count data.

    for i in myList:
        count.setdefault(i, 0) # Creates key in dictionary for each unique item in list, with default value of 0.
        count[i] = count[i] + 1 # Adds 1 to count for each occurence of item type.

    resultsFile.write('\nTypes: ' + str(len(count)) + '\n') # Prints length of dictionary (e.g. number of types)
    resultsFile.write('Tokens: ' + str(len(myList)) + '\n') # Prints length of list (e.g. number of tokens)
    resultsFile.write(json.dumps(count) + '\n\n\n') # Prints dictionary (e.g. count for each type)

# Edit this regex to find relevant words and phrases. Use pipe to separate multiple items.
myRegex = re.compile(r'food security|environment|sustainability', re.I)

# Edit this file path to save results in different location. 
resultsFile = open(Path.home() / 'results.txt', 'a')

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
        resultsFile.write(os.path.join(path, file)) # Prints name and location of file.
        content = open(os.path.join(path, file), 'r')
        text = content.read().lower() # Converts text to lowercase to avoid duplication in type count.
        result = myRegex.findall(text) # Creates a list of all words or phrases matching regex.
        typesTokensCount(result)

resultsFile.close()
print('Done.')
