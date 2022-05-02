from tkinter import *

window=Tk()

def kg_convertor():
    print(e1_value.get())
    km_to_grams=float(e1_value.get())*1000
    km_to_pounds=float(e1_value.get())*2.20462
    km_to_ounces=float(e1_value.get())*35.274
    t1.insert(END, km_to_grams)
    t2.insert(END, km_to_pounds)
    t3.insert(END, km_to_ounces)

b1=Button(window, text="Execute",command=kg_convertor)
b1.grid(row=0,column=3)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1,column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1,column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1,column=2)

window.mainloop()