x = int(input("Podaj liczbę: "))
print()

y = float(x) %2 ==0
z = float(x) %3 ==0
k = x > 10
l = x == 7
rownanie = y and z and k or l

print("Liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba-", rownanie)