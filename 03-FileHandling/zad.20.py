# zad. 20

numbers = []
with open('numbers.txt') as file:
    for line in file:
        if int(line) % 2 == 0:
            numbers.append(int(line))
            
with open('evennumbers.txt', 'w+') as file:
    for x in numbers:
        file.write(str(x) + '\n')