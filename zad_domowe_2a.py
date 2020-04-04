print("Gdzie znajduje się gracz na planszy?")
x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Gracz znajduje się poza planszą.")
elif 0 <= x <= 10:
    if 0 <= y <= 10:
        print("Gracz znajduje się w lewym dolnym rogu.")
    elif 10 < y < 90:
        print("Gracz znajduje się na lewej krawędzi.")
    elif 90 <= y:
        print("Gracz znajduje się w lewym górnym rogu.")
elif 10 < x < 90:
    if 0 <= y <= 10:
        print("Gracz znajduje się na dolnej krawędzi.")
    elif 10 < y < 90:
        print("Gracz znajduje się w centrum planszy.")
    elif y >= 90:
        print("Gracz znajduje się na górnej krawędzi.")
elif 90 <= x:
    if y <= 10:
        print("Gracz znajduje się w dolnym prawym rogu.")
    elif 10 < y < 90:
        print("Gracz znajduje się na prawej krawędzi.")
    elif y >= 90:
        print("Gracz znajduje się w prawym górym rogu.")
else:
    print("Rozwiązujący nie przewidział wszystkich przypadków...")