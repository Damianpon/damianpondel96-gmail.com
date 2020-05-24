##setOfNumbers = {1, 2, 4, 5, 6, 7, 8, 9, 10}
##setOfNumbers2 = {3, 3, 4, 5, 6}

##print(set(range(101)))

zbior = set()

while True:
    polecenie = input("Wpisz liczbę lub k by zakończę: ")
    if polecenie == "k":
        break
    zbior.add(int(polecenie))

liczby_parzyste = set(range(0, 101, 2))

print(len(zbior))
print(len(zbior & liczby_parzyste))
