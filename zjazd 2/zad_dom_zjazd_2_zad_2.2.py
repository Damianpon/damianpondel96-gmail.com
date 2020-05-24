listaaa = [-2, 10, 0,	5, 1, 16, 9]

def tworzymyNowaListe(poczatek, koniec):
    nowa_lista = listaaa[poczatek:koniec]
    return nowa_lista

def test_tworzymyNowaListe__():
    assert tworzymyNowaListe(1, 2) == [1]
    assert tworzymyNowaListe(0, 1) == [0]

print(tworzymyNowaListe(1, 2))