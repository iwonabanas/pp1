# zad.22. Dane są boki trójkąta a, b oraz c. Napisz program, który dla podanych boków obliczy pole trójkąta wykorzystując
# wzór Herona. Wartości boków trójkąta odczytaj z klawiatury.
# Korzystając z programu oblicz pole trójkąta dla wielkości boków 3, 4 i 5.

from math import sqrt

# Błąd gdy bok <= 0 
class Error(Exception):
    pass

try:
    a = float(input("Podaj a: "))
    if a <= 0:
        raise Error
    
    b = float(input("Podaj b: "))
    if b <= 0:
        raise Error
    
    c = float(input("Podaj c: "))
    if c <= 0:
        raise Error
    
    p = (a + b + c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    
    print("Pole trójkąta o bokach długości {:g}, {:g}, {:g} wynosi {:.4f}".format(a,b,c,S))
    
except ValueError:
    print("Podana wartość jest nieprawidłowa lub taki trójkąt nie istnieje!")
    
except Error:
    print("Bok trójkąta nie może być mniejszy niż 0!")