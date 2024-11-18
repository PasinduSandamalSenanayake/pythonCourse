from tkinter import *
from tkinter import messagebox #messagebox is the another model and so it is not in *
from random import *
import pyperclip # purpose of this library is does want to copy generated text to paste(click ctrl +v)
import json

# Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password) # show the generated password in UI
    pyperclip.copy(password) # When click the generate button and generated a password. Then someone want to paste password that he doesn't want to copy it because it automatically copied.That is the wonder of pyperclip.



# Save the file

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # create a new dictionary
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if (len(website) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    # message box
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError: # file not exist
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file: # when using this way do not use the data_file.close() end of the function
                #json.dump is save the data in th edata.json file
                json.dump(data, data_file, indent=4) # indent is used to easy way to understand the json format
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END) #(0, END) 0 means start of the text and END means end of the text

# find password

def find_password():
    web_site = website_input.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if web_site in data:
            email = data[web_site]["email"]
            password = data[web_site]["password"]
            print(f"{email} - {password}")
            messagebox.showinfo(title=f"{web_site} details", message=f"email = {email}\npassword = {password}")
            website_input.delete(0, END)
        else:
            messagebox.showinfo(title="Wrong web site", message="Please enter valid web site")
            website_input.delete(0, END)

# UI Design

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#DFF2EB")

canvas = Canvas(width=200, height=200, bg="#DFF2EB")
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

name_label = Label(text="Website:", bg="#DFF2EB")
name_label.grid(row=1, column=0)

website_input = Entry(width=32)
website_input.grid(row=1, column=1)

search_button = Button(text="Search", bg="#7AB2D3", width=14, command=find_password)
search_button.grid(row=1, column=2)

name_email = Label(text="Email/Username:", bg="#DFF2EB")
name_email.grid(row=2, column=0)

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2) # columnspan means , How many columns its span, column=1 is the starting column
email_input.insert(0, "sandamal@gmail.com") # 0 means start point of the text, default text


name_password = Label(text="Password:", bg="#DFF2EB")
name_password.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=generate_password, bg="#7AB2D3")
generate_button.grid(row=3, column=2)


add_button = Button(text="Add", width=43, command=save, bg="#4A628A")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()