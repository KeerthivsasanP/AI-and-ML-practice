from tkinter import *

converter_window = Tk()
converter_window.config(padx=20,pady=20)


mile_entry = Entry(width=10)
mile_entry.insert(0,"0")
mile_entry.grid(row=0,column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)

equal_label = Label(text="is equal to ")
equal_label.grid(row=1,column=0)

km_value = Label(text="0")
km_value.grid(row=1,column=1,padx=30)

km_label= Label(text="Km")
km_label.grid(row=1,column=2)

def convert_miles():
    miles = float(mile_entry.get())
    km = miles*1.609
    km_value.config(text=km)

cal_button = Button(text="Calculate",command=convert_miles)
cal_button.grid(row=2,column=1)


converter_window.mainloop()


