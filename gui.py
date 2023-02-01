from tkinter import*
window = Tk()

ent=Entry(window)
Tex1 =Label(window,text="Username",bg="gray")
Tex1.grid(column=0,row=0)

Tex2 =Label(window,text="password",bg="gray")
Tex2.grid(column=0,row=1)

ent=Entry(window,bg="aqua")
ent.grid(column=1,row=0)

ent2=Entry(window,bg="aqua")
ent2.grid(column=1,row=1)

but= Button(window, text='Login', bg="aqua", fg="blue")
but.grid(column=2,row=2)

window.mainloop()
