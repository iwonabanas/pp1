# zad.16

import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)  

for _ in cyfry:
    x = int(cyfry[0])
    y = int(cyfry[1])
    z = int(cyfry[2])
    
average_temperature = (x + y+ z)/len(cyfry)
print(average_temperature)  
