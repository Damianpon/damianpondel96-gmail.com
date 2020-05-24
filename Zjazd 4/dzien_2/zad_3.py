import tkinter
from tkinter import messagebox
def licz_koszt_przejazdu():
    try:
        val_a = int(a_entry.get())
        val_b = int(b_entry.get())
        mnozenie = val_a * val_b
        wynik.configure(text=mnozenie)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")
root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Odległość w kilometrach")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="Cena paliwa za 1 kilometr")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()
wynik_labl = tkinter.Label(master=root, text="Koszt przejazdu :")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text="Policz", command=licz_koszt_przejazdu)
submit.pack()
root.mainloop()
print("Po mainloop")