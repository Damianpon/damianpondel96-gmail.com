class Emplyee:

    num_of_emplyess = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        #self.full_name = first + " " + last

        Emplyee.num_of_emplyess += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Emplyee("Corey", "Schafer", 50000)
emp_2 = Emplyee("Test", "User", 60000)

Emplyee.set_raise_amt(1.05)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Emplyee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
emp_str_1 = "John-Doo-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Emplyee.from_string(emp_str_1)
print(new_emp_1.email)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Emplyee.is_workday(my_date))