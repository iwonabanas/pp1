# zad. 23

import re

with open('land.txt') as file:
    numbers = re.findall('\d', file.read())
    
numbers = [int(i) for i in numbers]
print(sum(numbers))