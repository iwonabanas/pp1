# zad. 21

numbers = []
with open('numbersinrows.txt') as file:
    for line in file:
        numbers += line.split(',')
        
numbers = [int(x) for x in numbers]

print('Ilość liczb: {}\nSuma: {}'.format(len(numbers), sum(numbers)))