from tkinter import *
from typing import Text
import phonenumbers as ph
from phonenumbers import geocoder, carrier

oni = Tk()

oni.title('LOCATION TRACKER')
oni.geometry('400x300')
label = Label(oni, text='Advance Project', height=2,font=("Felix Titling", 20)).pack()

ent = Entry(oni, width=30, borderwidth=3)
ent.pack()
ent.insert(0, "+(Country Code)(Number)")
ent.configure(state=DISABLED)

# on click func


def on_click(event):
    ent.configure(state=NORMAL)
    ent.delete(0, END)


ent.bind("<Button-1>", on_click)


# Main Func

def called():
    ch_num = ph.parse(ent.get(), "CH")
    ser_num = ph.parse(ent.get(), "RO")
    time_zone = ph.parse(ent.get())
    myLabel = Label(oni, text=geocoder.description_for_number(ch_num, "en")).pack()
    myLabel2 = Label(oni, text=carrier.name_for_number(ser_num, "en")).pack()


bt = Button(oni, text="Find", font=("Felix Titling", 10),bg='white', fg='black', command=called).pack()

oni.mainloop()
