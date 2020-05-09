class Produkt:

    def __init__(self, id, nazwa, cena):
        self.cena = cena
        self.id = id
        self.nazwa = nazwa


    def print_info(self):
        print(f"Produkt \"{self.nazwa}\", id: \"{self.id}\", cena: \"{self.cena} PLN\"")

produkt = Produkt(1, "Woda", 10.99)
produkt.print_info()