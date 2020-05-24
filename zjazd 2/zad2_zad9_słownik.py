##w = dict("marchewka" : 5, "ziemniaki": 2.25, "burak": 4, "pomarańcze": 2.5, "gruszka": 4, "pomidory": 4.15, "cebula": 1.99, "kalafior": 3.28)
products = {"marchewka": 5, "ziemniaki": 2, "burak": 4, "pomarańcze": 2.5, "gruszka": 4, "pomidory": 4.15,
            "cebula": 1.99,
            "kalafior": 3.28}
magazyn = {"marchewka": 10, "ziemniaki": 10, "burak": 10, "pomarańcze": 10, "gruszka": 10, "pomidory": 10, "cebula": 10,
           "kalafior": 10}

while True:
    komenda1 = input("Co chcesz zrobić? [k-kup] [z-zakończ] [m-magazyn] ")
    if komenda1 == 'z':
        break
    elif komenda1 == "k":
        product = input("Podaj co chcesz kupic: ")

        if product in products:
            ile = input(f"Ile kilogramów chcesz kupić {products[product]}? ")
            ile = float(ile)
            print(f"Za {ile} kg {product} zapłacisz {ile * products[produt]}")

            if ile < magazyn[product]:
                print(f"Za {ile} kg {product} zapłacisz {ile * products[product]}")
                magazyn[product] = magazyn[product] - ile
            else:
                print("Nie mamy tyle produktów")
    elif komenda1 == "m":
        produkt = input("Wpisz nazwę nowego produktu: ")
        ile = input("Wpisz ilość drugiego produktu ")
        magazyn[produkt] = magazyn.get(produkt, 0) + ile
        if newProduct not in magazyn:
            cena = float(input(f'Jaka cena za {newProduct}))
            products[produkt] = cena
        print(magazyn)
else:
    print("Niezrozumiała komenda")
