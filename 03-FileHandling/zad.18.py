# zad. 18

numbers_list = []
with open("numbers.txt", 'r') as tekst:
    for line in tekst:
        numbers_list.append(int(line))
numbers_list.sort()
for n in numbers_list:
    print(n, end=' ')
