length = int(input("Wprowadź długość przyprostokątnej: "))
listA = []
for i in range(1, length):
    listA.append(i)

lengthOfTheLastOne = len(listA)
for y in range(lengthOfTheLastOne):
    print("*" + " " * y + "*")
print("*" * length)
