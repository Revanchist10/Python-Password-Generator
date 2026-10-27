import random
import tkinter as tk
from tkinter import ttk

#variables and lists
root = tk.Tk()
var = tk.IntVar()
var1 = tk.IntVar()

length = 12

weak = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()+=-[{]}"
password = [""]
last_element = password[-1]
#functions
def generate():
    global password
    password = ""    
    tk.Label(root, text = "                                             p", font = 'arial 10 bold').place(x=150, y = 150)
    #if var is 1 do password_low
    if var.get()==1:  
        weak
        for i in range (0,length):
            password = "".join(random.choice(weak) for i in range(length)) #choose 12 random characters in the "weak" list and join them together
        tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
        password_low = ""
    #if var is 0 do medium
    elif var.get()==0:
        medium
        for i in range (0,length):
                password = "".join(random.choice(medium) for i in range(length)) #choose 12 random characters in the "medium" list and join them together
        tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
    #if var is 3 do strong
    elif var.get()==3:
            strong
            for i in range (0,length):
                password = "".join(random.choice(strong) for i in range(length)) #choose 12 random characters in the "strong" list and join them together
            tk.Label(root, text = password, font = 'arial 10 bold').place(x=150, y = 150)
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
radio_strong = ttk.Radiobutton(root, text = "Most Secure", variable = var, value = 3).place(x=25, y=175)

tk.mainloop()