x = "Ala ma kota"
z = len(x)

listA = []
for i in range(z):
    listA.append(x[i])
print(listA)
listaNaProbe = listA
w = listA
print(w)
listaB = []
for iles in range(z):
    suma = listA[iles] + w[iles] + listaNaProbe[iles]
    for que in range(1):
        listaB.append(suma)
print(listaB)

for elemka in listaB:
    wtf = str(elemka)
    print(wtf[2], end='')