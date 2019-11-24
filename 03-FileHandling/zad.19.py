# zad. 19

universities_list = []
with open('universities.txt', 'r') as file:
    for line in file:
        universities_list.append(line.strip('"'))

universities_list.sort()

with open('universities.txt', 'w') as file:
    for university in universities_list:
        file.write(university)