# zad. 13. Niech x i y oznaczają współrzędne punktu na płaszczyźnie.
# Napisz program, który określi, w której ćwiartce układu współrzędnych znajduje się punkt P(x,y)
# lub na której z osi jest on położony lub też że znajduje się on w początku układu współrzędnych.
 # !!! POPRAWIĆ

try:
    x = float(input('Podaj liczbę x: '))
    y = float(input('Podaj liczbę y: '))
    if x == 0 and y == 0:
        print(f"Punkt P ({x},{y}) znajduje sie w początku ukladu wspołrzędnych.")
     elif x == 0:
        print(f'Punkt P({x},{y}) znajduje się na osi X') 
    elif y == 0:
        print(f'Punkt P({x},{y}) znajduje się na osi Y')
    elif x > 0 and y > 0:
        print(f'Punkt P({x},{y}) znajduje się w I ćwiartce')
    elif x < 0 and y > 0:
        print(f'Punkt P({x},{y}) znajduje się w II ćwiartce')
    elif x < 0 and y < 0:
        print(f'Punkt P({x},{y}) znajduje się w III ćwiartce')
    elif x > 0 and y < 0:
        print(f'Punkt P({x},{y}) znajduje się w IV ćwiartce')

except ValueError:
    print('Podana wartość nie jest liczbą!')