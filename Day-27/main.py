from tkinter import *

window = Tk()
window.title("My first Programme")
window.minsize(500, 300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack() # show tha label

my_label["text"] = "New Text"

# Button
def button_clicked():
    my_label["text"] = input.get() # Show the entered text in the label when click the button

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=20)
input.pack()


# text

text = Text(height=5, width=30)
text.focus()
text.insert(END,"Example of multi line text entry.")
print(text.get("1.0", END))
text.pack()

# Spinbox

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# check button

def checkbutton_used():
    print(checked_state.get()) # Print 1 if On button checked, otherwise 0.

checked_state = IntVar() # 0 or 1
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()



# Radio Button

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# ListBox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fuirts = ["Apple", "Pear", "Orange", "Banana"]
for item in fuirts:
    listbox.insert(fuirts.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()













window.mainloop()  #Keep the window live