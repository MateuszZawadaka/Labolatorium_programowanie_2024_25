import random
import matplotlib.pyplot as plt
import numpy
print(type(1+1)) #int
print(type(3/2)) #float
print(type(4/2)) #float
print(type(3//2)) #int
print(type(-3//2))
print(type(11%2))
print(type(2**10))
print(type(2**(1/3)))
#<class 'int'>
##<class 'float'>
#<class 'float'>
#<class 'int'>
#<class 'int'>
#<class 'int'>
#<class 'int'>
#<class 'float'>
int(3.0) # --> zmienia typ ze całkowitą na zmiennoprzecinkowa
float(3) # --> zmienia typ ze zmiennoprzecinkowej na całkowitą
float("3") # --> zmienia typ ze str na zmiennoprzecinkową
str(12.4) # --> zmienia typ ze zmiennoprzecinkowego na str(string -> napis)
bool(0) # --> zamiana na zmienną boolowską 0 = FALSE, 1 = TRUE 


#Zad2

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

#Zad3
name = "Jan"
age = 20
height = 178
print("Nazywam się: ", name, "i mam: ",age, "lat.", end="\n")
print("Mój wzrost to: ", height, "cm")



# Zad. 4:
# Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat przypisz
# wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu podanego
# rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie formatowanie tekstu w
# funkcji print() tak, aby końcowa cena produktu została wyświetlona tylko do drugiego
# miejsca po przecinku.

price = 39.99
discount = 0.2
newPrice = price * (1 - discount)
print(f"Cena po rabacie: {newPrice:.2f} zł")
# Zad. 5:
# Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
# oraz wyświetla wyniki na ekranie.

def myfunction(x, y):
    if x<0 or y<0:
        return "jedna z długości mniejsza od zera"
    circuit = 2*x + 2*y
    surface = x*y
    print("Obwód: ", circuit, end="\n")
    print("Pole powierzchni: ", surface)

x= float(input("Podaj x: "))
y= float(input("Podaj y: "))

myfunction(x=x, y=y)



# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
# spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o
# szacowanych kosztach podróży (cena paliwa 6.5 zł/l).
# A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
# (liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.
# B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.
# Podpowiedź:
# import random - wykorzystanie w pliku biblioteki pozwalającej na wykorzystywanie
# funkcji pseudolosowych los = random.randint(-2, 5) - czytanie do zmiennej los losowej liczby
# z zakresu <-2, 5>
# help(random.randint) - Wyświetlenie pomocy na temat funkcji losującej liczby całkowite
# Python umożliwia tworzenie formatowanych łańcuchów tekstowych (stringów), których
# zawartość zależy od zmiennych, wchodzących w jego skład. Przed tego typu łańcuchem
# tekstowym wstawiamy literę f, natomiast zmienne do łańcucha wstawiamy w nawiasach
# klamrowych Na przykład:

#distance_km = float(input("Podaj dystans: "))
distance_km = random.randint(20, 2000)
fuelCOnsumption_lp100km = float(input("Średnie spalanie: "))
fuelPrice = 6.5
fuelCOnsumption_lp1km = fuelCOnsumption_lp100km/100
cost_zl = distance_km * fuelCOnsumption_lp1km * fuelPrice
print(f"Całkowity koszt: {cost_zl:.2f} zł, aby przejechać {distance_km}")


# Zad. 7:
# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania ro wnania
# liniowego ax + b = 0 , gdzie a i b są wspo łczynnikami podawanymi przez uz ytkownika

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b:"))
x = numpy.linspace(-100, 100, 100)


def plot(func):
    plt.figure(figsize=(12, 8))
    x = numpy.linspace(-100, 100, 100)
    y = a * x + b
    plt.plot(x, y, '-', color='blue')
    plt.show()
    plt.close()


plot(lambda x: x + 0.5)

# Zad. 8:
# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania ro wnania
# kwadratowego ax2 + bx + c = 0, gdzie a, b i c są wspo łczynnikami podawanymi przez
# uz ytkownika.
asqrt = float(input("Podaj współczynnik a: "))
bsqrt = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
x = numpy.linspace(-100, 100, 100)


def plotsqrt(func):
    plt.figure(figsize=(12, 8))
    x = numpy.linspace(-100, 100, 100)
    fx = asqrt * x**2 + bsqrt + c
    plt.plot(x, fx, '-', color='blue')
    plt.show()
    plt.close()


plotsqrt(lambda x: x + 0.5)

# Zad. 9:
# Napisz kalkulator, który wyświetli wyniki dodawania, odejmowania, mnożenia, dzielenia i
# potęgowania 2 liczb podanych przez użytkownika.

number1 = float(input("POdaj pierwsza liczbe: "))
number2 = float(input("Podaj druga liczbe: "))

print(f"Wynik dodawania{number1 + number2}", end="\n")
print(f"Wynik odejmowania{number1 - number2}", end="\n")
print(f"Wynik mnożenia{number1 * number2}", end="\n")
if number2 == 0:
    number3 = float(input("Podaj liczbe inną niż 0"))
    print(f"Wynik dzielenia{number1 / number3}", end="\n")  
else:
    print(f"Wynik dzielenia{number1 / number2}", end="\n")    
