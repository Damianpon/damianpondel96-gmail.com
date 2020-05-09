##5. Zdefiniuj funkcję foo, która przyjmie dowolną liczbę argumentów pozycyjnych i kluczowych
##   funkcja ma wypisać na ile ich jest


#foo(10, 20, a=1, b=2, c=3)
#   pozycyjnych: 2
#   kluczowych:  3

def foo(*args,**kwargs):
    liczba_args = []
    liczba_kwargs = []
    for i in args:
        liczba_args.append(i)
    for j in kwargs:
        liczba_kwargs.append((j))

    print(f' pozycyjnych: {len(liczba_args)}')
    print(f' kluczowych: {len(liczba_kwargs)}')

    return ""
print((foo(10, 20, a=1, b=2, c=3)))