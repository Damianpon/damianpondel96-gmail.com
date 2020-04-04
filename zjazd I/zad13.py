x = 7
temperatura = 0

while x > 0:
    t = int(input("Wprowadź temperaturę: "))
    x = x - 1
    temperatura += t

print(f"Średnia: {temperatura/7}")