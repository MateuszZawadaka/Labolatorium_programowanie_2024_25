from time import sleep
ilosc_paliwa_l = float(input("Podaj ilość paliwa w litrach: "))
zuzycie_paliwa_lns = float(input("Podaj zużycie paliwa w litrach na sekundę"))

def function(paliwo, zuzycie):
    licznik = 1
    while paliwo > 0:
        paliwo = paliwo - zuzycie
        sleep(1)
        licznik +=1
        print(f"Pozostało: {paliwo} litrów")
    print("koniec lotu")


function(ilosc_paliwa_l, zuzycie_paliwa_lns)