digitsToBeConverted = input("Wpisz ciąg liczb do przekształcenia: ")
digitsToBeConvertedToString = str(digitsToBeConverted)
numberOfDigitsToBeRead = len(digitsToBeConvertedToString)
print(numberOfDigitsToBeRead)


outDictionary = {1: "jeden", 2: "dwa", 3: "trzy", 4:"cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziwięć", 10: "dziesięć"}


for myLetter in range(numberOfDigitsToBeRead):
    if myLetter == digitsToBeConvertedToString.count(myLetter):
        print(outDictionary[myLetter])