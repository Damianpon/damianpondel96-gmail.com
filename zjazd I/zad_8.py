x = float(input("Podaj szerokość w cm: "))
y = float(input("Podaj długość w cm: "))
h = float(input("Podaj wysokość w cm: "))
v = x * y * h
result = v > 1000
print(f"Czy objętość opakowania wynosi {v} i jest ona większa od 1 litra?")
print(result)