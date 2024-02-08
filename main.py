from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(200, 120)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


my_label = Label(text="Miles", font=("Arial", 10))
my_label.grid(column=2, row=0)
my_label.config(width=10)

is_equal_label = Label(text="is equal to", font=("Arial", 10))
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="KM", font=("Arial", 10))
km_label.grid(column=2, row=1)

button = Button(command=miles_to_km, width=7, text="Calculate")
button.grid(column=1, row=3)


window.mainloop()