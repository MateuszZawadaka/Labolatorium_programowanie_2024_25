drogi = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

ilosc_budynkow = 5
ilosc_mieszkan = 10

def stworz_adresy(drogi, ilosc_budynkow, ilosc_mieszkan):
    wyniki = []
    
    for droga in drogi:
        for budynek in range(1, ilosc_budynkow + 1):
            for mieszkanie in range(1, ilosc_mieszkan + 1):
                adres = f"{droga} {budynek}/{mieszkanie}"
                wyniki.append(adres)
    
    return wyniki

wszystkie_adresy = stworz_adresy(drogi, ilosc_budynkow, ilosc_mieszkan)

for adres in wszystkie_adresy:
    print(adres)
