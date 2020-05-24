
""""

Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale',3 )
Wynik:
{'a', ' '}

"""
def wiecej_niz(text, prog):
    zbior = set()
    for znak in set(text):
        if text.count(znak) > prog:
            zbior.add(znak)

    return zbior

print(wiecej_niz("ala ma psa", 3))

def test_test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 4) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaa bbbb ccc dd e", 0) == {"a", "b", "c", "d", "e", " "}
    assert wiecej_niz("aaaaa bbbb ccc dd e", 3) == {"a", "b", " "}

