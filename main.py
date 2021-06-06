from tkinter import *

FONT = ('Arial', 12, "bold")
YELLOW = "#f7f5dd"
GOLDEN = "#DEDCC5"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_input = Entry(width=35, highlightthickness=0, relief="flat", bg=GOLDEN)
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(width=35, highlightthickness=0, relief="flat", bg=GOLDEN)
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21, highlightthickness=0, relief="flat", bg=GOLDEN)
password_input.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()