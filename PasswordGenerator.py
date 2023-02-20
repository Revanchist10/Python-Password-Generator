import random
import tkinter as tk
from tkinter import ttk

#variables and lists
root = tk.Tk()
var = tk.IntVar()
var1 = tk.IntVar()

length = 12

lower = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz"
medium = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz1234567890"
strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()+=-[{]}"
password = [""]
password_low = ""
last_element = password[-1]
#functions
def generate():
    global password
    password = ""    
    tk.Label(root, text = "                                             p", font = 'arial 10 bold').place(x=150, y = 150)
    #if var is 1 do password_low
    if var.get()==1:  
        global lower
        global password_low
        for i in range (0,length):
            password = "".join(random.choice(lower) for i in range(length)) 
        tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
        password_low = ""
    #if var is 0 do medium
    elif var.get()==0:
        global medium
        for i in range (0,length):
                password = "".join(random.choice(medium) for i in range(length))
        tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
    #if var is 3 do strong
    elif var.get()==3:
            global strong
            for i in range (0,length):
                password = "".join(random.choice(strong) for i in range(length))
            tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
#create tkinter window
root.title("Random Password Generator")
root.geometry('300x300')
#Generate button window labels
tk.Label(root, text = "Random Password Generator", font = 'arial 15 bold').pack()
tk.Label(root, text = "Pick a Password strength", font = 'arial 10 bold').place(x= 60, y= 25)
tk.Button(root, text = 'Generate', font = 'arial 10', command= generate, ).place(x=160, y= 220)
#buttons for choosing password strength
radio_low = ttk.Radiobutton(root, text = "Low", variable = var, value = 1).place(x=25, y=75)
radio_medium = ttk.Radiobutton(root, text = "Medium", variable = var, value = 0).place(x=25, y=125)
radio_strong = ttk.Radiobutton(root, text = "Strong", variable = var, value = 3).place(x=25, y=175)

tk.mainloop()