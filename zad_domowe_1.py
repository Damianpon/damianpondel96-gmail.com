print("Gdzie znajduje się gracz na planszy?")
position_of_X = int(input("Podaj pozycję gracza X: "))
position_of_Y = int(input("Podaj pozycję gracza Y: "))

if position_of_X <= 0 or position_of_Y <= 0:
    print("Gracz znajduje się poza planszą")
elif position_of_X <= 40:
    if position_of_Y <= 40:
        print("Gracz znajduje się w lewym dolnym rogu")
    elif position_of_Y > 40 and position_of_Y < 60:
        print("Gracz znajduje się w lewym centralnym rogu")
    elif position_of_Y >= 60 and position_of_Y <= 100:
        print("Gracz znajduje się w lewym górnym rogu")
elif position_of_X > 40 and position_of_X < 60:
    if position_of_Y <= 40:
        print("Gracz znajduje się w środkowej części na dole planszy")
    elif position_of_Y > 40 and position_of_Y < 60:
        print("Gracz znajduje się w środkowej części na środku planszy")
    elif position_of_Y >= 60 and position_of_Y <= 100:
        print("Gracz znajduje się w środkowej części na górze planszy")
elif position_of_X >= 60 and position_of_X <= 100:
    if position_of_Y <= 40:
        print("Gracz znajduje się w prawej dolnej części planszy")
    elif position_of_Y > 40 and position_of_Y < 60:
        print("Gracz znajduje się w prawej środkowej części planszy")
    elif position_of_Y >= 60 and position_of_Y <= 100:
        print("Gracz znajduje się w prawej górnej części planszy")
else:
    print("Gracz znajduje się poza planszą")
