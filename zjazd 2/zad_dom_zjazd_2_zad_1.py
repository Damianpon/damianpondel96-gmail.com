def palinondrom(napis):
    odwrotnie = napis[::-1]
    print(odwrotnie)
    if odwrotnie == napis:
        return "Tak, jest polinondrom"
    else:
        return "Nie, nie jest nim"


def test_polinondrom_123():
    assert palinondrom("kajak") == "Tak, jest polinondrom"
    assert palinondrom("python") == "Nie, nie jest nim"