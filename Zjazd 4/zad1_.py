#with open("test.txt") as f:
#    f.write("To jest pierwsza linia\n")
#    f.write("Druga linia\n")
#    f.write("trzecia linia\n")

with open("python_test.txt") as f:
    text = f.read()
    text = text.splitlines()
    for i, line in enumerate(text, start=1):
        print(f"{i}: {line}")
