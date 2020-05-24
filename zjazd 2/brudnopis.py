""" Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie. """

produkty = {"pomidory": 4, "malina": 8, "banan": 2, "jabło": 4.4}
magazyn = {"pomidory": 10, "malina": 10, "banan": 10, "jabło": 10}

lista_zakupow = {}
kosztZakupu = []

print("Dzień dobry")
while True:
    print("Co chcesz zrobić z [zakończyć] k [kupować] p [płacić]")
    co_robimy = input("Chce: ")

    if co_robimy == "z":
        print("Do widzenia i zapraszamy ponownie!")
        break
    elif co_robimy == "k":
        print("Oferujemy: ")
        for item in produkty.items():
            a, b = item
            print(a, "za", b, "zł/kg")
        print("Co chcesz kupić?")
        chce = input("Chce kupić: ")
        if chce in produkty:
            print("Ile kilogramów potrzebujesz?")
            ile = float(input()).__round__(3)
            if ile < magazyn[chce]:
                koszt = ile * b
                kosztZakupu.append(koszt)
                lista_zakupow[a] = koszt
                magazyn[chce] = magazyn[chce] - ile
                print("Za te produkty będzie", koszt, "zł.")

            else:
                print("Niestety nie mamy wystarczająco. Ile chcesz?")
                ile = float(input()).__round__(3)
                koszt = ile * b
                kosztZakupu.append(koszt)
                lista_zakupow[a] = koszt
                magazyn[chce] = magazyn[chce] - ile
                print("Za te produkty będzie", koszt.__round__(3), "zł.")
        else:
            print("Niestety nie mamy. Zamówimy na jutro!")

    elif co_robimy == "p":
        suma = sum(kosztZakupu)
        print(lista_zakupow)
        print("Suma wszystkich zakupów wynosi: ", suma.__round__(3), "zł.")
