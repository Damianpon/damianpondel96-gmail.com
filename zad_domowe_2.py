print("Gdzie znajduje się gracz na planszy?")
x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Gracz znajduje się poza planszą.")
elif x >= 0 and x <= 10 and y >= 0 and y <= 10:
    print("Gracz znajduje się w lewym dolnym rogu.")
elif x > 10 and x < 90 and y >= 0 and y <= 10:
    print("Gracz znajduje się na dolnej krawędzi.")
elif x >= 90 and y <= 10:
    print("Gracz znajduje się w prawym dolnym rogu.")
elif 0 <= x <= 10 and 10 < y < 90:
    print("Gracz znajduje się na lewej krawędzi.")
elif 0 <= x <= 10 and y >= 90:
    print("Gracz znajduje się na lewym górnym rogu.")
elif 10 < x < 90 and y >= 90:
    print("Gracz znajduje się na górnej krawędzi.")
elif x >= 90 and y >= 90:
    print("Gracz znajduje się na prawym górnym rogu.")
elif x >= 90 and 10 < y < 90:
    print("Gracz znajduje się na prawej krawędzi.")
elif 10 < x < 90 and 10 < y < 90:
    print("Gracz znajduje się w centrum planszy.")
else:
    print("Rozwiązujący nie uwzględnił wszystkich przydadków.")
