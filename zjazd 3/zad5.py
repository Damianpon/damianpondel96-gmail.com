class CashMashine:
    def __init__(self, lista):
        self.lista = lista

        self.lista = list(lista)

    @property
    def is_available(self):
        if len(self.lista) > 0:
            return True
        else:
            return False

    def put_money(self, money):
        money = list(money)
        for i in money:
            self.lista.append(i)

        return lista



class TestCashMashine:
    def test_init(self):
        cash_mashine = CashMashine([])
        assert cash_mashine
    def test_cash_is_available(self):
        cash_mashine = CashMashine([])
        assert cash_mashine.is_available == False
    def test_put_money(self):
        cash_mashine = CashMashine([200, 100, 100, 50])
        assert cash_mashine.put_money([200, 100, 100, 50]) == [200, 100, 100, 50]

    #[200, 100, 100, 50]