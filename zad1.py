liczba_punktow = float(input("Podaj liczbę zdobytych punktów: "))

if liczba_punktow > 80:
    print("Zaliczyłeś w terminie 0")
elif liczba_punktow >= 50 and liczba_punktow < 80:
    print("Zaliczyłeś w terminie 0 jednak możesz poprawić swój wynik")

else:
    print("Musisz poprawić egzamin")
