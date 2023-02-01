import tkinter as tk

def button1_click():
    print("Homework")

def button2_click():
    print("write")

window = tk.Tk()


button1 = tk.Button(window, text="Button 1", command=button1_click)
button2 = tk.Button(window, text="Button 2", command=button2_click)

button1.pack()
button2.pack()

window.mainloop()
