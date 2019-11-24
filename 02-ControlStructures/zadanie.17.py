# zad.17. Napisz program, który obliczy sumę liczb parzystych oraz nieparzystych z przedziału <1,50>.

poz = 0
neg = 0

for x in range (1,51):
    if x % 2 == 0:
        poz += x
    else:
        neg += x
        
print(f'Przedział <1,50>\nSuma liczb parzystych: {poz}\nSuma liczb nieparzystych: {neg}')