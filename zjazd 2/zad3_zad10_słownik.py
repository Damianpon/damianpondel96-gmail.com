napis = "ala ma kota"
zliczenia = dict() # {}

for znak in napis:
    if znak in zliczenia:
        zliczenia[znak] = zliczenia[znak] + 1
    else:
        zliczenia[znak] = 1

print(zliczenia)