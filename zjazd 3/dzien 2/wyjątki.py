class ExceptionPojemnikFull(Exception):
    pass



class Pojemnik:

    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity

    def add_element(self, element):
        if len(self.elements) == 10:
            raise ExceptionPojemnikFull("Capacity przekroczone")
        self.elements.append(element)


p = Pojemnik(10)

for i in range(20):
    p.add_element(i)

print(p.elements)
