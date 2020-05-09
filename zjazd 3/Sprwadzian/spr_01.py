##3. Zaimplementuj funkcję realizującą algorytm sortowanie przez wybieranie
def wymieranie_przez_sortowanie(lista):
    for i in range(len(lista)):
        wart_min = i
        for j in range(1 + i, len(lista)):
            if lista[j] < lista[wart_min]:
                wart_min = j
        lista[i], lista[wart_min] = lista[wart_min], lista[i]

    return lista

print(wymieranie_przez_sortowanie([9, 1, 6, 8, 4, 3, 2, 0]))

