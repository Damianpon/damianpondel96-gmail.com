class CashMachine:

    def __init__(self):
        self.__money = []

    @property
    def cash_is_available(self):
        return len(self.__money) > 0

    def put_money_into(self, bills):
        self.__money += bills

    def withdraw_money(self, amount):
        to_withdraw = []

        for bill in sorted(self.__money, reverse=True):
            if sum(to_withdraw) + bill <= amount:
                to_withdraw.append(bill)

            if sum(to_withdraw) == amount:
                for bill in to_withdraw:
                    self.__money.remove(bill)
                return to_withdraw







class TestCashMashine:

    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_money_there(self):
        cash_machine = CashMachine()
        assert cash_machine.cash_is_available == False


    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money_into([200, 100, 100, 50])
        assert cash_machine.cash_is_available == True

    def test_withdraw(self):
        cash_machine = CashMachine()
        cash_machine.put_money_into([200, 100, 100, 50])
        assert cash_machine.withdraw_money(150) == [100, 50]