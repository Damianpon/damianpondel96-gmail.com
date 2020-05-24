import json

"""
load - odczytywanie danych z pliku (deserializacja)
dump - zapisywanie danych do pliku (serializacja)
loads - odczyt danych z testu
dumps - serializacja do tekstu
"""

text = '{"a":2, "b":4}'

dane = json.loads(text)

print(dane)
print(type(dane))

x = {i: i**3 for i in range(10)}
print(x, type(x))

print(json.dumps(x))