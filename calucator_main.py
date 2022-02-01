from tkinter import *
 
def add_numbers():
    res = float(e1.get())+ float(e2.get())+ float(e3.get())+ float(e4.get())+ float(e5.get())+ float(e6.get())
    res = round(res,4)
    label_text.set(res)


window = Tk()
window.geometry("450x300")

label_text=StringVar();
Label(window, text="Number:").grid(row=0, column=0,sticky=W)
Label(window, text="Number:").grid(row=1,column=0, sticky=W)
Label(window, text="Number:").grid(row=2,column=0, sticky=W)
Label(window, text="Number:").grid(row=3,column=0, sticky=W)
Label(window, text="Number:").grid(row=4,column=0, sticky=W)
Label(window, text="Number:").grid(row=5,column=0, sticky=W)
Label(window, text="Total Amount:").grid(row=6,column=0, sticky=W)
result=Label(window, text="", textvariable=label_text).grid(row=6,column=1, sticky=W)
 
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window)
e6 = Entry(window)

 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

 
b1 = Button(window, text="Add", width=10,command=add_numbers)
b1.grid(row=0, column=2, padx=5, pady=5,sticky=W)
 

window.mainloop()