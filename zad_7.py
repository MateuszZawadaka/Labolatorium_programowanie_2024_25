def srednia(oceny, studenci):
    suma_punktow = 0 
    for i in range(studenci):
        suma_punktow += oceny[i]

    srednia_punktow = suma_punktow / studenci
    return srednia_punktow

ilosc_studentow = int(input("Podaj ilość studentów: "))
punkty = []
x = 1
while x <= ilosc_studentow:
    punkty_dla_studenta = float(input(f"Podaj liczbę punktów dla studenta nr: {x}:  "))
    punkty.append(punkty_dla_studenta)
    x += 1

srednia_punktow = srednia(punkty, ilosc_studentow)
print(f"Średnia punktów: {srednia_punktow}")
