# Zdefiniuj klasę Student, która będzie dziedziczyć po klasie Osoba. Student w czasie tworzenia wymaga podania dodatkowego atrybutu
# - kierunek. W metodzie info należy rozszerzyć działanie metody info z klasy rodzica. Nie należy jednak całkowicie jej nadpisywać
#
# student = Student("Johny", "Bravo", 2000, "physics")
# assert osoba.age == 20
# assert osoba.info == "Johny Bravo (20) - physics"
import datetime


class Osoba:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.age = datetime.datetime.now().year - birth_year

    @property
    def info(self):
        return f" Imię: {self.name}, nazwisko: {self.last_name}, wiek: {self.age}"


# osoba = Osoba("Johny", "Bravo", 2000)
# print(osoba.info)


class Student(Osoba):

    def __init__(self, kierunek):
        super().__init__("Student", kierunek)

student = Student("Johny", "Bravo", 2000, "physics")
print(student.info)
