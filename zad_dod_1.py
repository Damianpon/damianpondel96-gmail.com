a = "HELLO\nWORLD!"

## Splice a string to get characters at even index
## print("Even index: ", str1[::2])

## print(::1])
b: str = str(input("Wpisz co mam wyświetlić: "))
print(b[0:100:2],sep=" ")
print(b[1:100:2],sep=" ")

napis = input("Podaj napis: ")

x = napis[::2]
y = napis[1:3] + napis[7::2]

print(x, sep=' ')
print(y, sep=' ')