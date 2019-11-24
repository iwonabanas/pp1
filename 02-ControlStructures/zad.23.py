# 23. Ocena stanowi umowny sposób zakwalifikowania postępów ucznia lub studenta.
# Może zostać przedstawiona w zapisie symbolicznym (np. cyfry od 1 do 6) lub słownym.
# Napisz program, który dla wartości numerycznej oceny odczytanej z klawiatury wyświetli jej słowny zapis
# (celujący, bardzo dobry, dobry, dostateczny, mierny, niedostateczny). Umieść nazwy ocen w tablicy.

class NotAGradeError(Exception):
    """ Gdy podana wartość nie mieści się w skali 1-6 """
    pass

oceny = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']

try:
    x = int(input('Podaj ocenę: '))
    if x <= 0 or x > 6:
        raise NotAGradeError
    print(f'Ocena słownie: {oceny[x-1]}')
except ValueError:
    print('Podana wartość nie jest liczbą!')
except NotAGradeError:
    print('Podana wartość nie jest oceną 1-6!')