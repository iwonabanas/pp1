
# zad.21 - Napisz program, który dla podanej wartości temperatury wyrażonej w stopniach Celsjusza odczytanej z klawiatury
# wyznaczy temperaturę w stopniach Fahrenheita oraz Kelvina.

# przeliczanie st. Celsjusza na Kelvina i na Fahrenheita
try:
    t = int(input("Podaj temperaturę w C: "))
    print(f"{t}C to {float(t)+273.15}K")
    print(f"{t}C to {float(9/5*t)+32}F")
except ValueError:
    print("Podana wartość nie jest liczbą!")
    
