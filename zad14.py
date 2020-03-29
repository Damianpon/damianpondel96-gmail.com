min_x = None
max_x = None
while True:
    nowaliczba = input("Wprowadź liczbę: ")
    if nowaliczba == "x":
        break
    nowaliczba = int(nowaliczba)
    if min_x is None or nowaliczba < min_x:
        min_x = nowaliczba
    if max_x is None or nowaliczba > max_x:
        max_x = nowaliczba

print("MAX",max_x)
print("MIN",min_x)
