x = int(input("Wprowadź liczbę gwiazdek kwadratu: "))
a = (x * "* ")
b = len(a)

print(a)
for i in range(x - 2):
        print("*" + (b - 3) * " " + "*")
print(a)

print("")
print(b)
