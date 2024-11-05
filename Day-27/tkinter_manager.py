from tkinter import *

window = Tk()
window.title("My first Programme")
window.minsize(500, 300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)# show tha label
my_label.config(padx=10, pady=10)

my_label["text"] = "New Text"

# Button
def button_clicked():
    my_label["text"] = "Sandamal"

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

#Entry

input = Entry(width=20)
input.grid(column=2, row=0)

button_new = Button(text="me")
button_new.grid(column=4, row=3)
button_new.config(padx=10, pady=10)



















window.mainloop()