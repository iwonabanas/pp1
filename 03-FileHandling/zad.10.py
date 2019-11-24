# zad.10 Plik numbers.txt zawiera wykaz liczb naturalnych. Napisz program obliczający sumę tych liczb.
# Wskazówka: odczytaj kolejny wiersz z pliku i dokonaj jego konwersji do wartości numerycznej.

suma = 0
with open ('numbers.txt', 'r') as file:
    for line in file:
        suma += int(line)
    
print("Suma liczb z pliku numbers.txt wynosi: ", suma)   
    