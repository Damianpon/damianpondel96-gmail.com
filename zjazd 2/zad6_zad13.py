print([x/10 for x in range(11)])

print({(x, x**2, x**3) for x in range(-10, 11)})

napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxxxxxxxxxx"}

print({napis:len(napis) for napis in napisy})
