# 14. Napisz program do obliczania wieku psa w psich latach. Przez pierwsze dwa lata, rok życia psa wynosi 10,5 ludzkiego roku.
# Potem każdy rok psa wynosi 4 ludzkie lata. Przykładowy rezultat:

class NegativeError(Exception):
    """ Błąd, gdy wiek jest wartością ujemną """
    pass

try:
    age = int(input("Podaj wiek psa w ludzkich latach: "))
    if age < 0:
        raise NegativeError
    elif age <= 2:
        age_dog = age*10.5
    else:
        age_dog = 21 + (age-2)*4
    print(f"Wiek psa w psich latach to {age_dog} lata")
    
except ValueError:
      print('Podana wartość nie jest liczbą!')
      
except NegativeError:
    print('Wiek nie może być ujemny!')
    
