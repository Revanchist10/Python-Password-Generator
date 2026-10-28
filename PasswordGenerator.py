import random
import tkinter as tk
from tkinter import ttk
import string

#variables and lists
root = tk.Tk()
var = tk.IntVar()

password_display =  tk.Label(root, text = "", font = 'arial 10 bold')
password_display.place(x=150, y = 150)
length = 12

weak = string.ascii_letters
medium = string.ascii_letters + string.digits
custom_symbols = "!@#$%&"
strong = string.ascii_letters + string.digits + custom_symbols
password = [""]
#functions
def generate():
    global password
    password = ""    
    #if var is 1 do weak
    if var.get()==1:  
        password = "".join(random.choice(weak) for i in range(length)) #choose 12 random characters in the "weak" list and join them together
        password_display.config(text = password)
    #if var is 0 do medium
    elif var.get()==0:
        password = "".join(random.choice(medium) for i in range(length)) #choose 12 random characters in the "medium" list and join them together
        password_display.config(text = password)
    #if var is 3 do strong
    elif var.get()==2:
        password = "".join(random.choice(strong) for i in range(length)) #choose 12 random characters in the "strong" list and join them together
        password_display.config(text = password)
#create tkinter window
root.title("Random Password Generator")
root.geometry('300x300')
#Generate button window labels
tk.Label(root, text = "Random Password Generator", font = 'arial 15 bold').pack()
tk.Label(root, text = "Pick a Password strength", font = 'arial 10 bold').place(x= 60, y= 25)
tk.Button(root, text = 'Generate', font = 'arial 10', command= generate, ).place(x=160, y= 220)
#buttons for choosing password strength
radio_low = ttk.Radiobutton(root, text = "Basic", variable = var, value = 1).place(x=25, y=75)
radio_medium = ttk.Radiobutton(root, text = "More Secure", variable = var, value = 0).place(x=25, y=125)
radio_strong = ttk.Radiobutton(root, text = "Most Secure", variable = var, value = 2).place(x=25, y=175)

tk.mainloop()