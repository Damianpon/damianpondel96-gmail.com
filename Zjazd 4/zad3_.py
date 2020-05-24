with open("emails.txt.txt") as f:

    for line in f:
        out = []
        line = line.lower()
        line = line.lstrip()
        line = line.rstrip()
        out.append(line)
        out = set(out)


    for cos in out:
        if line[5] != "-":
            del cos
        if line[6] != "@":
            del cos

    print(out)



