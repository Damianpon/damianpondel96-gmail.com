## print('123'.replace('2',"a"))
digitsToBeConverted = input("Wpisz ciąg liczb do przekształcenia: ")
digitsToBeConvertedToString = str(digitsToBeConverted)
lenghtOfString = len(digitsToBeConvertedToString)
ourDictionary = {1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                 9: "dziwięć", 10: "dziesięć"}
myDictionary = ("jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziwięć", "dziesięć")
firstElement = (digitsToBeConvertedToString[0])

if digitsToBeConvertedToString["0"] == "0" or digitsToBeConvertedToString["1"] == "1" or digitsToBeConvertedToString[
    "2"] == "2" or digitsToBeConvertedToString["3"] == "3" or digitsToBeConvertedToString["4"] == "4" or \
        digitsToBeConvertedToString["5"] == "5" or digitsToBeConvertedToString["6"] == "6" or digitsToBeConvertedToString[
    "7"] == "7" or digitsToBeConvertedToString["8"] == "8" or digitsToBeConvertedToString["9"] == "9":
    a = digitsToBeConvertedToString[i].replace("0", "zero")
    b = digitsToBeConvertedToString[i].replace("1", "jeden")
    c = digitsToBeConvertedToString[i].replace("2", "dwa")
    d = digitsToBeConvertedToString[i].replace("3", "trzy")
    e = digitsToBeConvertedToString[i].replace("4", "cztery")
    f = digitsToBeConvertedToString[i].replace("5", "pięć")
    g = digitsToBeConvertedToString[i].replace("6", "sześć")
    h = digitsToBeConvertedToString[i].replace("7", "siedem")
    w = digitsToBeConvertedToString[i].replace("8", "osiem")
    v = digitsToBeConvertedToString[i].replace("9", "dziewięć")
print(a + b + c + d + e + f + g + h + w + v)
