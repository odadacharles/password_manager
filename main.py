from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
password = ""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    global password
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    site = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {
        site: {
            "email": email,
            "Password": pw,
        }
    }

    if len(site) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Incomplete Entry", message="Some fields are blank. Please provide all the details!")

    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def find_password():
    site = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="File Not Found!")
    else:
        if site in data:
            email = data[site]['email']
            pw = data[site]['Password']
            messagebox.showinfo(title=site, message=f"Email: {email} \n"
                                                    f"Password: {pw}")
        else:
            messagebox.showinfo(title="Error", message="Website not Found!")




# ---------------------------- UI SETUP ------------------------------- #
# color scheme
RED = "#F65A83"
PINK = "FF87B2"
YELLOW = "#FFE898"
CREAM = "FFF8BC"
FONT = 'Georgia'

# window
window = Tk()
window.title("Password Vault")
window.config(padx=50, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, sticky="ew")

# website label
website = Label(text="Website:", bg=YELLOW)
website.grid(column=0, row=1, sticky="ew")

# Email username label
user_email = Label(text="Username/Email:", bg=YELLOW)
user_email.grid(column=0, row=2, sticky="ew")

# Password label
password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(column=0, row=3, sticky="ew")

# website entry
website_entry = Entry(width=15)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

# Email entry
email_entry = Entry(width=35)
email_entry.insert(0, "somethingsomething@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Generate password button
generate_pw = Button(text="Generate Password", command=password_generator)
generate_pw.grid(column=2, row=3, sticky="ew")

# Search Button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky='ew')

# Save button
save_to_file = Button(text="Save", width=35, command=save_entry)
save_to_file.grid(column=1, row=4, columnspan=2, sticky='ew')

window.mainloop()
