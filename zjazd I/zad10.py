first_number = int(input("Podaj pierwszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))
kind_of_operation = input("Podaj znak operacji: ")


if kind_of_operation == "+":
    result = first_number + second_number
elif kind_of_operation == "-":
    result = first_number - second_number
elif kind_of_operation == "*":
    result = first_number * second_number
elif kind_of_operation == "/":
    if second_number == 0:
        result = "Pamietaj cholero nie dziel przez zero"
    else:
        result = first_number / second_number
else:
    result = "Zła operacja"

print(f"Wynik: {result}")