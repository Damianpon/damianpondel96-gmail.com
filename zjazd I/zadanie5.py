city_a = str(input("Podaj nazwę miasta A: "))
city_b = str(input("Podaj nazwę miasta B: "))
distance = float(input("Podaj dystans pomiędzy miastami w kilometrach: "))
fuel_consumption = float(input("Podaj ilość spalonej benzyny nas 100 km: "))
fuel_cost = float(input("Podaj koszt benzyny na kilometr: "))

x = int(fuel_consumption * fuel_cost * (distance / 100))

print(f"Koszt przejazdu między {city_a} a {city_b} to {x} zł.")
