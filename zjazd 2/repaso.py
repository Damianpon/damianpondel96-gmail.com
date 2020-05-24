lata = []
listaa = []

for i in range(1990, 2020):
    lata.append(i)
    print(lata)


napis = "ala ma kota i kota ma ala"
my_dict = dict()
napis1 = napis.split(" ")
ile_powtorzen = len(napis1)

for wyraz in range(ile_powtorzen):
    x = napis1.count(napis1[wyraz])
    my_dict[napis1[wyraz]] = x

print(my_dict)