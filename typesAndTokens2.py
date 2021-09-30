# This program prints total types, total tokens and a count for each unique type of list item.

myListExample = ['A', 'B', 'B', 'C', 'D', 'D', 'D', 'D', 'D', 'A']

def typesTokensCount(myList):
    count = {} # Creates dictionary to hold the count data.

    for i in myList:
        count.setdefault(i, 0) # Creates key in dictionary for each unique item in list, with default value of 0.
        count[i] = count[i] + 1 # Adds 1 to count for each occurence of item type.

    print('Types: ' + str(len(count))) # Prints length of dictionary (e.g. number of types)
    print('Tokens: ' + str(len(myList))) # Prints length of list (e.g. number of tokens)
    print(count) # Prints dictionary (e.g. count for each type)

typesTokensCount(myListExample)
