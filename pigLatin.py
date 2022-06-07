#English to Pig Latin
#Pig Latin is a silly made-up language that alters English words. If a word begins with a vowel, the word yay is added to the end of it. 
#If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay

print( "\n" 'Enter an English Message to transalte into Pig Latin: ')

message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

#intialize words in Pig Latin(Empty list)
pigLatin = []

for word in message.split():
    #separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.appemd(prefixNonLetters)
        continue
    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))
