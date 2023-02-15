import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers)for char in range(nr_numbers)]
    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    # for char in password_list:
    #     password+=char

    # print(f"Your password is: {password}")
   
    password_input.insert(0,f"{password}")
    pyperclip.copy(password) 


    # ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("/home/sameeranati/password_manager/manager.json","r") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.ERROR(title="error",text="This data file doesnot exist")
    else:
        website=website_input.get()
        # print(f"{data[website]} {website}")
    
        if website in data:
            messagebox.askokcancel(title=f"Search Information:{website}", message=f"Email:{data[website]['email']}\nPassword:{data[website]['password']}")
        else:
            messagebox.showinfo(title="error",text="This website doesnot exist")
        
        
            
        
        


def add_text():
    new_data={
        website_input.get():{
            "email":email_usename_input.get(),
            "password":password_input.get()
            }
            }
    # if len(website_input.get())!=0 or len(password_input.get())!=0:
    #     ok=messagebox.askokcancel(title=f"{website_input.get()}",message=f"These are details entered:\n Email:{email_usename_input.get()}\n Password:{password_input.get()}\n Is it ok to save?")
    if len(website_input.get())!=0 or len(password_input.get())!=0:
        try:
            f=open("/home/sameeranati/password_manager/manager.json","r")
            data=json.load(f)
        except FileNotFoundError:
            f=open("/home/sameeranati/password_manager/manager.json","w")
            json.dump(new_data,f,indent=4)
           

        else:
            f=open("/home/sameeranati/password_manager/manager.json","r")
            # f.write(f"{website_input.get()} | {email_usename_input.get()} | {password_input.get()} \n")
            # json.dump(new_data,f,indent=4)
            #reading data
            # data=json.load(f)
            #updating data
            data.update(new_data)
            #writing data
            with open("/home/sameeranati/password_manager/manager.json","w") as file:
                json.dump(data,file,indent=4)
        
        finally:
            website_input.delete(0,'end')
            password_input.delete(0,'end')
    else:
        messagebox.showerror(title="oops", message="Please don't leave any fields empty! ")
        

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("PASSWORD MANAGER")
# window.minsize(width=300,height=300)
window.config(padx=50,pady=50,bg="White")
canvas=tkinter.Canvas(width=200,height=200,bg="white",highlightthickness=0)
t=tkinter.PhotoImage(file="/home/sameeranati/password_manager/logo.png")
canvas.create_image(100,100,image=t)
canvas.grid(row=0,column=1)
website_label=tkinter.Label(text="Website:",bg="white")
website_label.grid(column=0,row=1)
email_username_label=tkinter.Label(text="Email/Username:",bg="white")
email_username_label.grid(column=0,row=2)
password_label=tkinter.Label(text="Password:",bg="white")
password_label.grid(column=0,row=3)

website_input=tkinter.Entry(width=17)
website_input.grid(row=1,column=1)
website_input.focus()


email_usename_input=tkinter.Entry(width=35)
email_usename_input.grid(row=2,column=1,columnspan=2)
email_usename_input.insert(0,"sameeranati@gmail.com")

password_input=tkinter.Entry(width=16)
password_input.grid(row=3,column=1)


generate_password_button=tkinter.Button(text="Generate Password",command=password_generator)
generate_password_button.grid(row=3,column=2)

add_button=tkinter.Button(text="Add",width=33, command=add_text)
add_button.grid(row=4,column=1,columnspan=2)

search_button=tkinter.Button(text="Search",width=17,command=search)
search_button.grid(row=1,column=2)




window.mainloop()