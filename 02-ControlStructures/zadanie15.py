# zad.15. Napisz program, który utworzy tabliczkę mnożenia w zakresie od 1 do 10, dla dowolnej liczby wprowadzonej przez użytkownika.

try:
    x = float(input("Podaj liczbę: "))
    for i in range (1,11):
        print("{0:g} x {1} = {2:g}".format(x,i,x*i))
    
except ValueError:
    print("Podana wartość nie jest liczbą!")
    
    