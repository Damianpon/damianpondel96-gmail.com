k = int(input("Wpisz stan początkowy: "))
n = int(input("Wpisz ilość lat: "))
p = float(input("Wpisz oprocentowanie już podzielone przez odpowiednią liczbę: "))
n1 = int(input("Wpisz liczbę kapitalizacji: "))

stanKoncowy = k * ((1 + (p / 100)) ** n1)

print(f"Po {n} latach, przy oprocentowaniu {p}% będziemy mieć do dyspozycji {stanKoncowy} złotych.")

stanKoncowy1 = k * (1 + (p/(100 * k)) ** (n1 * k))

print(f"Po {n} latach, przy oprocentowaniu {p}% będziemy mieć do dyspozycji {stanKoncowy1} złotych.")