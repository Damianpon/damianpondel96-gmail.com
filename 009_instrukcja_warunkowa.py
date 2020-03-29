# Pełnoletność osoby
import datetime

year_of_birth = int(input("Podaj rok urodzenia: "))
curreny_year = datetime.datetime.now().year
print(f"Obecny rok to: {curreny_year}")
your_age = curreny_year - year_of_birth
if your_age >= 18:
    print("Brawo! Jesteś pełnoletn!")
else:
    print("Nie jesteś pełnoletni...")







