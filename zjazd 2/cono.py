lista = [9, 1, 6, 8, 4, 3, 2, 0]

for i in range(len(lista)):
    wart_min = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[wart_min]:
            wart_min = j

    lista[i], lista[wart_min] = lista[wart_min], lista[i]

print(lista)