elementy = [1, 2, 3, 4, 5, "xxx", 2.0, 2]

print((type(elementy)))
print(list())


# Lista jest mutowalna --> można ją edytować

x = elementy.append("cos")
print(elementy)
print(x)

print(len(elementy))

while len(elementy) <11:
    elementy.append("xx")

print(dir(elementy))