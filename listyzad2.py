lista = []
while len(lista) < 10:
    x = input("Wprowadź liczbę: ")
    lista.append(x)
print(sum(lista)/len(lista))