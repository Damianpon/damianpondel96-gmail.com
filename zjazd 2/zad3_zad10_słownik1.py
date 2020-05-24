napis = "ala ma kota"
zliczenia = {}

for znak in napis:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

print(zliczenia)