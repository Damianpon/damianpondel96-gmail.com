class Basket():
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.price
        return total_price

class Product():

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class BasketEntry():

    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount

    @property
    def count_entry_price(self):
        entry_price = self.amount * self.product.price
        return entry_price


class TestBasket():

    def test_basket(self):
        basket = Basket()
        assert basket

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert basket.products[0].product == product
        assert basket.products[0].amount == 5

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product, 5)
        basket.add_product(product2, 5)
        assert basket.count_total_price() == 5 * 10.0 + 5 * 2.00


class TestProduct():

    def test_init(self):
        product = Product(1, "Woda", 10.00)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10.00


class TestBasketEntry():

    def test_init(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.product == product
        assert be.amount == 5

    def test_entry_price(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.count_entry_price == 5 * 8

