""" Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie. """

produkty = {"pomidory": 4, "malina": 8, "banan": 2, "jabłko": 4.4}
magazyn = {"pomidory": 10, "malina": 10, "banan": 10, "jabłko": 10}

lista_zakupow = []
while True:
    co_robic = input("Powiedz co chcesz zrobić: \n Wpisz z [zakończycz] k [kupować] p [płacić]  ")

    if co_robic == "z":
        print("Do widzenia!")
        break
    elif co_robic == "k":
        print("W sklepie oferujemy: ")
        for item in produkty.items():
            a, b = item
            print(a, "za", b, "zł/kg")
        print("Co chcesz kupić ")
        produkt = input()
        if produkt in produkty:
            print("Ile potrzebujesz kilogramów: ")
            ile = int(input("Potrzebuję "))
            if ile < magazyn[produkt]:
                a = ile * produkty[produkt]
                lista_zakupow.append(a)
                print(f"Za {ile} kg {produkt} zapłacisz {a:.2f}")
                magazyn[produkt] = magazyn[produkt] - ile
                print(lista_zakupow)
            else:
                print("Niestety nie mamy wystraczająco. Ile chcesz?")
                ile = int(input("Potrzebuję "))
                if ile < magazyn[produkt]:
                    a = ile * produkty[produkt]
                    lista_zakupow.append(a)
                    print(f"Za {ile} kg {produkt} zapłacisz {a:.2f}")
                    magazyn[produkt] = magazyn[produkt] - ile
                    print(lista_zakupow)
        else:
            print("Niestety nie mamy")
    elif co_robic == "p":
        suma = sum(lista_zakupow)
        print("Za wszystkie produkty zapłacisz", suma, "zł")
