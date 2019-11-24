# zad.17
# findall ---> returns a list containing all matches

import re
sentence = 'To be, or not to be, that is the question'
vowels = re.findall('[aeiou]',sentence)

how_many_vowels = len(vowels)

print(how_many_vowels)

