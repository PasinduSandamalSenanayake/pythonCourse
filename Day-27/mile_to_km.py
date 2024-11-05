from tkinter import *

# Create window
window = Tk()
window.title("My First Program")
window.minsize(500, 300)

# Create entry widget for miles input
mile_entry = Entry(width=10)
mile_entry.grid(row=1, column=1, padx=50, pady=30)  # Use row and column for positioning

mile_text = Label(text="Miles", font=("Arial", 18))
mile_text.grid(row=1, column=2)

next_text = Label(text="is equal to", font=("Arial", 18))
next_text.grid(row=2, column=1)

km_answer_label = Label(text="0", font=("Arial", 14))
km_answer_label.grid(row=2, column=2)

km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(row=2, column=3)


def Button_Convert():
    mile = float(mile_entry.get())
    km = mile * 1.6
    km_answer_label.config(text=km)

button = Button(text="Calculate", command= Button_Convert)
button.grid(row=3, column=2)


# Run the main loop
window.mainloop()
