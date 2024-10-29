plik = open('notowania_gieldowe.txt', 'r')

for line in plik:
    print(line)

with open("notowania_gieldowe.txt", 'w') as file:
    file.write("ALR, 113")

with open("notowania_gieldowe.txt", 'r') as file:
    print(file.read())