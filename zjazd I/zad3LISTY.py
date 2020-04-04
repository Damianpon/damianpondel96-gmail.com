dane = [1, 2, 412, 41, -2, -1, 4, -2]
liczba_dod = 0
liczba_ujem = 0
for element in dane:
    if element > 0:
        liczba_dod = liczba_dod + 1
    else:
        liczba_ujem = liczba_ujem + 1

print("Ile jest liczb dodatnich?", liczba_dod)
print("Ile jest liczb ujemnych?", liczba_ujem)