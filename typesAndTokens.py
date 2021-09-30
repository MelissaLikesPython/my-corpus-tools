# This program finds and counts types and tokens in a list of strings.

myListExample = ['A', 'B', 'C', 'C', 'D', 'D', 'D', 'A']

def tokensAndTypes(myList):
    print(' '.join(myList)) # Concatenates and prints list as a string.
    print('Tokens: ' + str(len(myList))) # Prints number of words in list (tokens).

    myListTypes = list(dict.fromkeys(myList)) # Removes duplicates by creating dictionary with list items as keys, then creating new list.

    print(' '.join(myListTypes)) # Concatenates and prints list as string with duplicates removed (types).
    print('Types: ' + str(len(myListTypes))) # Prints number of words in list with duplicates removed (types).

tokensAndTypes(myListExample)
