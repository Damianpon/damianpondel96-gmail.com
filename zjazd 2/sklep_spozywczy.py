
produkty = {"pomidory": 4, "malina": 8, "banan": 2, "jabłko": 4.4}
magazyn = {"pomidory": 10, "malina": 10, "banan": 10, "jabłko": 10}

def sklep_spozywczy():
    lista_zakupow = dict()
    koszt = list()
    print("Dzień dobry! W czym możemy pomóc?")

    while True:
        print("Jeśli chcesz kupować to naciśnik- k, zapłacić- p, zakończyć- z")
        komenda = input("Chce: ")
        if komenda == "k":
            print("Nasz sklep oferuje: ")
            for item in produkty.items():
                a, b = item
                print(f"{a} za {b} zł/kg.")
            print("Co chcesz kupić")
            produkt = input("Kupuję: ")
            if produkt in produkty:
                print("Ile potrzebujesz? ")
                ile = float(input("Potrzebuję: "))
                if ile < magazyn[produkt]:
                    lista_zakupow[produkt] = (ile * b)
                    koszt.append(ile * b)
                    magazyn[produkt] = magazyn[produkt] - ile
                    print(f"Za {ile} kg {produkt} zapłacisz {ile * b:.2f} złotych.")
                else:
                    print("Niestety nie mamy wystarczająco. Ile podać?")
                    ile = float(input("Podaj: "))
                    lista_zakupow[produkt] = (ile * b)
                    magazyn[produkt] = magazyn[produkt] - ile
                    koszt.append(ile * b)
                    print(f"Za {ile} kg {produkt} zapłacisz {ile * b:.2f} złotych.")
        elif komenda == "p":
            suma = sum(koszt)
            print(f"Za wszystkie produkty zapłacisz {suma:.2f} złotych.")
            print("Tu masz paragon:")
            for itemy in lista_zakupow.items():
                c, d = itemy
                print(f"{c}, {d:.2f} zł")
            print(f"Suma {suma:.2f} zł.")
        elif komenda == "z":
            return  "Dziękujemy za zakupy, zapraszamy ponownie!"
        else:
            print("Wpisz poprawną komendę!")



print(sklep_spozywczy())
