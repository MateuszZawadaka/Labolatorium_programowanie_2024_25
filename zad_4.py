x = int(input("Ilość osób: "))
n = int(input("Ilość potraw: "))
cena = 0
i = 1
kwota = 0
while i <= n:
    cena = float(input(f"Podaj cene potrawy{i}: "))
    kwota = kwota + x * cena
    i += 1

print(f"Kwota za wszytko{kwota}")
na_osobe = kwota / x
print(f"Kwota na osobę: {na_osobe}")