def lista_lat_przestepnych(poczatek, koniec):
    lata = []
    listaa = []

    for i in range(poczatek, koniec + 1):
        lata.append(i)
        ileToLat = len(lata)
    for rok in lata:
        if rok % 4 == 0 and rok % 100 or rok % 400 == 0:
            listaa.append(rok)


    return listaa



def test_sprawdz_lata():
    assert lista_lat_przestepnych(1990, 2020) == [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

print(lista_lat_przestepnych(1990, 2020))