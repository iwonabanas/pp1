# tworzę generator liczb losowych z zakresu 1-6
# wykonuję trzy ruty kostką do gry
import random

first = random.randint(1, 6)
second = random.randint(1, 6)
third = random.randint(1, 6)

# wyświetlam rezultat trzech rzutów kostką do gry
print(first)
print(second)
print(third)

# sumuję wyrzucone oczka
sum = first + second + third

# wyświetlam sumę wyrzuconych oczek
print(sum)