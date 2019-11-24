# zad. 22

import re

students_list = []
with open('students.txt') as file:
    
    for line in file:
        item = re.findall('\d+[^@,]', line)
        
        if item and int(item[0]) < 30:
            item = line.split(',')
            print('{:7} {:9} {}'.format(item[0], item[1], item[4]), end='')