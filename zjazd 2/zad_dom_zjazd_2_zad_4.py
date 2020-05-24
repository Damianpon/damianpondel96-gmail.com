# napis = "ala ma kota i kota ma ala"
def licz_wyrazy(napis):
    my_dict = dict()
    napis1 = napis.split(" ")
    ile_powtorzen = len(napis1)

    for wyraz in range(ile_powtorzen):
        x = napis1.count(napis1[wyraz])
        my_dict[napis1[wyraz]] = x

    return my_dict

def test_licz_wyrazy():
    assert licz_wyrazy("ala ma kota i kota ma ala") == {'ala': 2, 'ma': 2, 'kota': 2, 'i': 1}