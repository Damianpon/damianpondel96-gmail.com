
curr_year = 2020
first_name = str(input("Imię: "))
last_name = input("Nazwisko: ")
b_year = int(input("Podaj rok urodzenia: "))
profession = str(input("Podaj zawód: "))
print("")

age = curr_year - b_year
print(age)

result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}
=============================
rok urodzenia:      {b_year}
zawód:              {profession.lower()}
"""
