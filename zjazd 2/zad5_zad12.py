lista = [9,1,6,8,4,3,2,0]

for indeks_podstawienie in range(len(lista)):
    indeks_min_wartości = indeks_podstawienie
    for indeks_ogona in range(indeks_podstawienie + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wartości]:
            indeks_min_wartości = indeks_ogona

    lista[indeks_podstawienie], lista[indeks_min_wartości] = lista[indeks_min_wartości], lista[indeks_podstawienie]
print((lista))
