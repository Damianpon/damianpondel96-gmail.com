import tkinter
from tkinter import messagebox

def licz_koszt_przejazdu():
    try:
        val_a = int(a_entry.get())
        val_b = int(b_entry.get())
        val_c = int(c_entry.get())
        mnozenie = (val_a * val_b * val_c)/100
        wynik.configure(text=mnozenie)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Odległość w kilometerach")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Koszt za litr")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()


c_label = tkinter.Label(master=root, text="Benzyna na 100 kilometrów")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()


wynik_label = tkinter.Label(master=root, text="Koszt przejazdu")
wynik_label.pack()
wynik = tkinter.Label(master=root, text="")
wynik.pack()
submit = tkinter.Button(master=root, text="Policz", command=licz_koszt_przejazdu)
submit.pack()

root.mainloop()
