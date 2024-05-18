from tkinter import *
from tkinter import messagebox
import random

WHITE = '#000000'
alphabets = 'abcdefghijklmnopqrstuvwxyz'
special_char =  '!@#$%^&*()_+,.'

#------------ Generate password ------------

def gen_password():
    random_password = ""

    lowercase_count = random.randint(2,5)
    uppercase_count = random.randint(2,5)
    special_char_count = 12-(lowercase_count+uppercase_count)

    password_list = []

    for _ in range(lowercase_count):
        random_password = random_password + alphabets[random.randint(0,25)]

    for _ in range(uppercase_count):
        random_password = random_password + alphabets[random.randint(0,25)].upper()
                                    
    special_char_len = len(special_char)
    for _ in range(special_char_count):
        random_password = random_password + special_char[random.randint(0,special_char_len - 1)]

    password_list = list(random_password)

    random.shuffle(password_list)

    random_password = ''
    for letter in password_list:
        random_password = random_password + letter
    if len(password_entry.get()) != 0:
        password_entry.delete(0,END)
    password_entry.insert(0,random_password)


#------------- Save password ---------------

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #messagebox.showinfo(title="Save",message="Do you want to save the credentials?")
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Mandatory fields",message="Password and website name are mandatory")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Email : {email}\n password : {password}\n Do you want to save?")
        if is_ok:
            with open("data.txt","a") as datafile:
                datafile.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


#------------- Creating UI ------------------
window = Tk()
window.config(padx=20,pady=20)

canvas = Canvas(heigh=252,width=200)

logo_image = PhotoImage(file="lock.png")
canvas.create_image(100,126,image=logo_image)
canvas.grid(row=0,column=1)

website_label = Label(text='Website : ')
website_label.grid(row=1,column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2)

username_label = Label(text='Username/Email : ')
username_label.grid(row=2,column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"example@email.com")

password_label = Label(text='Password : ')
password_label.grid(row=3,column=0)

password_entry = Entry(width=34)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text='Generate Password',command=gen_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=45,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
