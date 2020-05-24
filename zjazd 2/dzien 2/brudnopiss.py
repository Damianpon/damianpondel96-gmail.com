def filtruj(lista, poczatek, koniec):
    sortowane = sorted(lista)
    print(sortowane)
    lista2 = lista[poczatek, koniec]
    return lista2


def test_filtrujemy():
    assert filtruj([-2, 10, 0,	5, 1, 16, 9], 5, 15) == [10, 5, 9]