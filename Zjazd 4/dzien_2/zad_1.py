import json

try:
    with open("employees.json") as fp:
        listaa = json.load(fp)
except FileNotFoundError:
    listaa = []

while True:
    komenda = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")
    if komenda == "d":
        imiee = input("Wpisz imię: ")
        nazwisko = input("Wpisz nazwisko: ")
        rok_urodzenia = input("Wpisz rok urodzenia: ")
        pensja = input("Wpisz pensję: ")
        listaa.append((imiee, nazwisko, imiee+"."+nazwisko+"@gmail.com", rok_urodzenia, pensja))
    elif komenda == "w":
        with open("employees.json", "w") as fp:
            json.dump(listaa, fp)
