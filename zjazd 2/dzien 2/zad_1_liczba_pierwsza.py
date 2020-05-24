def liczby_pierwsze(x):
    if x == float() or x == int():
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            print("Liczba nie jest liczbą pierwszą")
        else:
            print("Liczba jest liczbą pierwszą")
    else:
        return "Wpisz liczbę"


print(liczby_pierwsze(x=9))


def czy_jest_pierwsza(liczba):
    for i in range(2, liczbaa):
        if liczba % i == 0:
            return False
    return True


if __name__ == "___main___":
    print("Wykonuje testy")
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(10) == False
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(17) == True

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(11) == False
    assert czy_jest_pierwsza(17) == True