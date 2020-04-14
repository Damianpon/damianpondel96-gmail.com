x = int(input("Wpisz ilość pożądanych boków: "))
lengthOfX = str(x)
numberOfSteps = lengthOfX

listA = []
listA1 = []

for k in range(1, x):
    listA1.append(k)
    reverselenght = len(listA1)
    for y in range(1, x, -1):
        listA.append(y)
        lengthOfTheLastOne = len(listA)
    lengthOfTheLastOne = 0
reverselenght = x

for i in range(x):
    print((reverselenght - 1) * " " + "/" + 2 * lengthOfTheLastOne * " " + "\\")
    lengthOfTheLastOne += 1
    reverselenght -= 1

for z in range(x):
    print(reverselenght * " " + "\\" + ((2 * lengthOfTheLastOne) - 2) * " " + "/")
    lengthOfTheLastOne -= 1
    reverselenght += 1

print(listA1)
print(listA)
