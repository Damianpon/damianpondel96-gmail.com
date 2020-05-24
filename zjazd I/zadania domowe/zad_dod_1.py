napis = input("Podaj napis: ")

x = napis[::2]
y = napis[1:3] + napis[7::2]
space1 = " ".join(x)
space2 = " ".join(y)

print(space1)
print(space2)

