## print('123'.replace('2',"a"))
digitsToBeConverted = input("Wpisz ciąg liczb do przekształcenia: ")
digitsToBeConvertedToString = str(digitsToBeConverted)
outDictionary = {1: "jeden", 2: "dwa", 3: "trzy", 4:"cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziwięć", 10: "dziesięć"}

print(digitsToBeConvertedToString.replace("1", "jeden") or digitsToBeConvertedToString.replace("2", "dwa") or digitsToBeConvertedToString.replace("3", "trzy"))