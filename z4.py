x = int(input("Wpisz ilość pożądanych boków: "))
lenthOfX = str(x)
numberOfSteps = 0
print(x * " " + "/\\")
for i in range(x - 1):
    print(numberOfSteps * " " + "\\")
    numberOfSteps += 1
for i in range(x - 1):
    print(numberOfSteps * " " + "/")
    numberOfSteps -= 1
print((x - 1) * " " + "\\ /")

print("")
print(lenthOfX)
print(x)

