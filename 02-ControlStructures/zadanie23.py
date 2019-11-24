# pobieramy ocenę odczytaną z klawiatury o wartości numerycznej

mark = input('Podaj ocenę: ')
print(input)
mark = int(mark)

if mark < 1 or mark > 6:
    print("Podaj wartość z zakresu 1-6")

markslist = ["celujący", "bardzo dobry", "dobry", "dostateczny", "mierny", "niedostateczny"]

if mark == 6:
    print(markslist[0])
if mark == 5:
    print(markslist[1])
if mark == 4:
    print(markslist[2])
if mark == 3:
    print(markslist[3])
if mark == 2:
    print(markslist[4])
if mark == 1:
    print(markslist[5])