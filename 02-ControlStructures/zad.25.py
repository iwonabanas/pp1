# 25. Napisz program, który narysuje prostokąt złożony z symboli gwiazdek o wymiarach 3 x 7.

# Prostokąt 3x7

for x in range(0,3):
    for y in range(0,7):
        print('*', end='')
    print()