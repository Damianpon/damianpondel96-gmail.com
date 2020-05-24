import tkinter
from tkinter import messagebox
from pogoda import get_location_id, get_location_weather, report

def przygotuj_raport():
    location_id = get_location_id(a_entry.get())
    weather = get_location_weather(location_id)
    rep = report(weather, a_entry.get())
    wynik.configure(text=rep)

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Wpisz miasto")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
wynik_labl = tkinter.Label(master=root, text="Dane odpośnie pogody :")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text="Szukaj", command=przygotuj_raport)
submit.pack()
root.mainloop()
