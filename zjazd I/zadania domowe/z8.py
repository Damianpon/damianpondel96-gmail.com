## ax2+bx+c=0, gdzie a, b i c

a = float(input("wprowadz liczbę a: "))
b = float(input("wprowadz liczbę b: "))
c = float(input("wprowadz liczbę c: "))
x1 = None
x2 = None
x0 = None
delta = (b ** 2) - (4 * a * c)
print("Delta równa się:", delta)
if delta == 0:
    x0 = -b / (2 * a)
    print("Pierwiastek jest równy", x0, ", lecz nie jest to równanie kwadratowe.")
elif delta > 0:
    x1 = (-b - (delta ** (1 / 2))) / (2 * a)
    x2 = (-b + (delta ** (1 / 2))) / (2 * a)
    print(f"Pierwiastek x1 jest równy {x1}, a pierwiastek x2 {x2}")
else:
    print("Brak wyniku")



