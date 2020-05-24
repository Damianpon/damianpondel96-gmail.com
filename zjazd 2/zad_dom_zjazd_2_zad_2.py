def nowa_lista_z_zakresu(poczatek, koniec):
    listaaa = []
    while True:
        co_robisz = input("Co robisz? l - tworze listę, z - przechodzę dalej ")
        if co_robisz == "l":
            srodek_listy = input("Stwórz listę: ")
            listaaa.append(srodek_listy)

        elif co_robisz == "z":
            nowa_lista = listaaa[poczatek:koniec]
            return nowa_lista

        else:
            return "Użyj poprawnej komendy"



def test_nowa_lista_z_zakresu():
    assert nowa_lista_z_zakresu(1, 2) == ["1"]

print(nowa_lista_z_zakresu(1, 2))


