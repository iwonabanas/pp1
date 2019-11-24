# zad.25. Numer rachunku bankowego składa się z 26 cyfr. Napisz program, który odczyta numer rachunku z klawiatury
# (wprowadzane tylko cyfry), a następnie wyświetli go w formacie jak poniżej (wraz z odstępami).

number = input("Podaj numer rachunku bankowego: ")
output = " "
temp = " "
try:
    int(number)
    print(f'Numer rachunku: {number[0:2]} {number[2:6]} {number[6:10]} {number[10:14]} {number[14:18]} {number[18:222]} {number[22:26]}')
    
except ValueError: 
    print("Podaj tylko cyfry!")