cityA = str(input("Podaj nazwę miasta A: "))
cityB = str(input("Podaj nazwę miasta B: "))
distance = float(input("Podaj dystans pomiędzy miastami w kilometrach: "))
fuelConsumption = float(input("Podaj ilość spalonej benzyny nas 100 km: "))
fuelCost = float(input("Podaj koszt benzyny na kilometr: "))

x = int(fuelConsumption * fuelCost * (distance / 100))

print(f"Koszt przejazdu między {cityA} a {cityB} to {x} zł.")
