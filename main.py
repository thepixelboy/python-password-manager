from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Arial', 12, "bold")
YELLOW = "#f7f5dd"
GOLDEN = "#DEDCC5"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(16, 18))]
  password_symbols = [choice(symbols) for _ in range(randint(4, 6))]
  password_numbers = [choice(numbers) for _ in range(randint(4, 6))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  password_input.insert(0, password)

  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  username = username_input.get()
  password = password_input.get()
  new_data = {
    website: {
      "username": username,
      "password": password,
    }
  }

  if len(website) == 0 or len(username) == 0 or len(password) == 0:
    messagebox.showwarning(message="Please make sure you haven't left any field empty.")
  else:
    try:
      with open("data.json", "r") as data_file:
        # reading old data
        data = json.load(data_file)
    except FileNotFoundError:
      with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
    else:  
        # updating old data with new data
        data.update(new_data)

        with open("data.json", "w") as data_file:
          # saving updated data
          json.dump(data, data_file, indent=4)
    finally:
          website_input.delete(0, END)
          username_input.delete(0, END)
          password_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
  website = website_input.get()

  try:
    with open("data.json", "r") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showwarning(message="No data file found.")
  else:
    if website in data:
      username = data[website]["username"]
      password = data[website]["password"]

      messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
    else:
      messagebox.showinfo(title=website, message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=YELLOW)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT, bg=YELLOW, pady=4)
website_label.grid(column=0, row=1, sticky="e")

username_label = Label(text="Email / Username:", font=FONT, bg=YELLOW, pady=4)
username_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:", font=FONT, bg=YELLOW, pady=8)
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_input = Entry(width=21, highlightthickness=0, relief="flat", bg=GOLDEN)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=35, highlightthickness=0, relief="flat", bg=GOLDEN)
username_input.grid(column=1, row=2, columnspan=2)
# username_input.insert(0, "email@domain.com")

password_input = Entry(width=21, highlightthickness=0, relief="flat", bg=GOLDEN)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()