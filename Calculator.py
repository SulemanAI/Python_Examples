from tkinter import *

root = Tk()

root.geometry("644x450")
root.title("Calculator By AI")
root.configure(background="silver")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="luada 40 bold").pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="7", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="8", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="9", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="5", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="6", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="1", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="2", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
b = Button(f, text="3", font='Arial 20', padx="24", pady="28")
b.pack(side="left")
f.pack()

root.mainloop()
