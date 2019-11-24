# zad. 24

names = [['Marek', 'Zelnik', 'zelnik@sed.pl'], [
    'Ewa', 'Maj', 'maje@wp.pl'], ['Piotr', 'Wyga', 'wygap@gop.pl']]

with open('plik.csv', 'w+') as file:
    file.write('Imie,Nazwisko,Email\n')
    
    for items in names:
        for item in items:
            file.write(item+',')
        file.write('\n')