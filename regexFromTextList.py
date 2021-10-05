# Creates regex from plain text list of words or phrases, in order to search for multiple strings.

content = open('/Users/melissacorlett/foodSecurityRegex.txt', 'r')
text = content.read().lower()
splitText = text.split('\n')
joinText = '|'.join(splitText)
print(joinText)
