# zad. 12. Zmienne x oraz y zawierają wartości całkowite wprowadzone z klawiatury.
# Napisz program, który sprawdzi, czy którakolwiek z tych zmiennych posiada wartość ujemną.

try:
    x = float(input("Podaj liczbę x: "))
    y = float(input("Podaj liczbę y: "))
    
    if x < 0 and y >= 0:
        print(f"Liczba {x} jest ujemna")
    elif y < 0 and x >= 0:
        print(f"Liczba {y} jest ujemna")
    elif y < 0 and x < 0:
        print(f"Podane liczby {x} i {y} są ujemne")
    else:
        print("Żadna z podanych liczb nie jest ujemna")
        
except ValueError:
    print("Podana wartość nie jest liczbą!")