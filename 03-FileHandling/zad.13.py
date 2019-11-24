# zad.13. Tablica zawiera następujące wartości całkowite: 32, 16, 5, 8, 24, 7. Napisz program
# zapisujący zawartość tablicy do pliku tekstowego, każda liczba w oddzielnym wierszu.

numbers_list = [32, 16, 5, 8, 24, 7]

with open('myfile.txt', 'w') as file:
    for number in numbers_list:
        liczby = print(number)
        file.write(str(number) + "\n")
        
        
    