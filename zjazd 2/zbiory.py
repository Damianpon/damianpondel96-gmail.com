zbior = set()
print(zbior)

zbior.add("x")
zbior.add(1)
print(zbior)

for element in zbior:
    print(element)

print(dir(zbior))

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)
print((a & b))
print(a - b)
print(a ^ b)

print(a.pop())
print(a)

print(dir(set()))