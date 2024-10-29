def obliczenie_bonusu(x):
    _bonus = x * 10
    if x >= 5 and x < 10:
        _bonus += 5
    elif x == 10:
        _bonus += 10
    elif x > 10:
        _bonus += 15

    return _bonus 

gol = int(input("Liczba strzelonych bramek: "))
bonus = int()

   
bonus = obliczenie_bonusu(gol)
print(f"ilość zdobytych punktów: {bonus + gol}")