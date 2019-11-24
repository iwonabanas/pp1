# zad.30. Tablica zawiera wartości: 12,6, 4, 9 oraz 3. Napisz program, który wartości tablicy wyświetli w formie graficznej

list = [12, 6, 4, 9, 3]
for item in list:
    counter = " "
    for x in range(item):
        counter += '*'
    print(str(item) + ": " + counter + "\n")