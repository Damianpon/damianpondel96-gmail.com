lista = [9, 1, 6, 8, 4, 3, 2, 0]
for indeks_podstawienia in range(len(lista)):
    indeks_min_wartosci = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wartosci]:
            indeks_min_wartosci = indeks_ogona
    # a, b  = b, a
    lista[indeks_podstawienia], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienia]
print(lista)
assert lista == [0, 1, 2, 3, 4, 6, 8, 9]

listaA = [9, 1, 6, 8, 4, 3, 2, 0]
for gdzie_jestem in range(len(listaA)):
    gdzie_zaczynam = gdzie_jestem
    for indeks_obecny in range(gdzie_jestem + 1, len(listaA)):
        if listaA[indeks_obecny] < listaA[gdzie_zaczynam]:
            gdzie_zaczynam = indeks_obecny
    listaA[gdzie_jestem], listaA[gdzie_zaczynam] = listaA[gdzie_zaczynam], listaA[gdzie_jestem]
print(f"Moje nazwy: {listaA}")
print(listaA)