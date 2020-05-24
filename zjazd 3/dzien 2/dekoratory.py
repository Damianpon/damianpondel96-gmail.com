import time

def milion_kwadratow():
    return len([x **2 for x in range(10000000)])


def mierz_czas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper()

@mierz_czas
def kwadraty():
    return len([n ** 2 for x in range(n)])

kwadraty = mierz_czas(kwadraty)

kwadraty(1000)

mierz_czas(milion_kwadratow)