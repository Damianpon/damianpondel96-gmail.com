## writeSthDown = input("Wpisz tekst: ")
writeSthDown = input("Wprowdź tekst: ")
lengthOfWriteSthDown = len(writeSthDown)
writeSthDown2 = writeSthDown
i = 0
for i in range(lengthOfWriteSthDown):
    if i % 2 == 0:
        u = writeSthDown[i]
        z = writeSthDown[i + 1] * 2
        print(u + z, sep="", end="")