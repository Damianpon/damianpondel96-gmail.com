def przywitanie():
    print("Hello world!")
    return "Hello world"

przywitanie()

x = przywitanie()

print(3, x)
def przywitanie1(name):
    text = f"Hello {name}"
    print(text)
    return text

przywitanie1("Rafal")
przywitanie1("Ilona")

def icrementator(poczatek, krok=1):
    return poczatek + krok

print(icrementator(18))
print(icrementator(14))

print(icrementator(13, 4))

def zlacz_teksty(lista_tekstow):
    return " ".join(lista_tekstow)

lista = ["A", "B", "C"]

print(zlacz_teksty(lista))

def zlacz_teksty(*lista_tekstow):
    print(lista_tekstow)
    return " ".join(lista_tekstow)

t1 = "A"
t2 = "B"
t3 = "C"
zlacz_teksty(t1, t2, t3)
zlacz_teksty(t1, t2)
zlacz_teksty((t1))

kolekcja = [(10, "z"), (5, "c"), (15, "a")]
print(sorted(kolekcja))
print(sorted(kolekcja, reverse=True))

def second(x):
    return x[1]

second = lambda x: x[1]
print(sorted(kolekcja, key=second, reverse=True))
print(sorted(kolekcja, key=second))

suma = lambda x, y: x + y
print((lambda x, y: x + y)(1, 2))
print(suma(1, 2))

lista_osob = ["Jan Nowak", "Anna Zagajska", "Mateusz Pospieszalski", "Piotr Baran"]
print(sorted(lista_osob, key=lambda x: x.split()[1]))


def decrement(n):
    if n == 0:
        print(0)
        return
    print(n)
    decrement(n-1)

decrement(10)

