# 18. Napisz program, który wyświetli liczby od 1 do 30. Jeśli liczba jest podzielna przez 3 to zamiast niej wyświetl słowo ‘THREE’,
# jeśli liczba jest podzielna przez 5 to wyświetl słowo ‘FIVE’.
# Natomiast jeśli liczba jest podzielna zarówno przez 3 jak i przez 5 to wyświetl słowo ‘BINGO’

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')