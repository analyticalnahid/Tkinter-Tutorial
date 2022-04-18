from tkinter import *
from tkinter import ttk, messagebox, filedialog
import time
import csv
import os

# Basic Setup
win = Tk()
win.title("GUI")
#win.iconbitmap('icon.JPG')
#win.maxsize(width= 300, height= 600)
#win.minsize(width=300, height=600)
#win.geometry('600x300')

# Label
lbl = Label(win, text="First Text", bg="red", fg="white",bd=2)
#lbl.pack()
#lbl.grid(column=5,row=5)
lbl.place(x=10, y= 10)

# Text-Input
def func():
    x = var.get()
    print(x)
    lbl1.config(text=x)

lbl1 = Label(win, text="Nothings", bg="red", fg="white",bd=2)    
lbl1.place(x=10, y=50)

var = StringVar()
ent = Entry(win, bg="green", fg="white",textvariable=var)
ent.place(x=10,y=90)

# Button
btn = Button(win, text="Submit", command=func)
btn.place(x=10,y= 130)

# Dropdown
dop = ttk.Combobox(win, width=27)
dop['values'] = ('Jan','Feb','Mar')
dop.current(0)
dop['state'] = 'readonly'
dop.place(x=10, y= 170)

# Checkbox 
def funcn():
    print(chck1.get())
    print(chck2.get())

chck1 = IntVar()
chck2 = IntVar()

box1 = Checkbutton(win, text="Male", variable=chck1, onvalue=1, offvalue=0)
box1.place(x=10, y = 210)

box2 = Checkbutton(win, text="Female", variable=chck2, onvalue=1, offvalue=0)
box2.place(x=10, y = 250)

btn = Button(win, text="Show Output", command=funcn)
btn.place(x=10, y= 290)


# Radio Button
def funcn():
    if var.get() == 1:
        print("On")
    else:
        print("Off")   

var = IntVar()

rdb1 = Radiobutton(win, text="On", value=1, variable=var)
rdb1.place(x=10, y= 330)

rdb1 = Radiobutton(win, text="Off", value=0, variable=var)
rdb1.place(x=10, y= 370)


btn = Button(win, text="Switch", command=funcn)
btn.place(x=10, y= 410)

# Frame 
top = Frame(win, bg="green")
top.pack(side=TOP)
bottom = Frame(win, bg= "red")
bottom.pack(side=BOTTOM)

lbl1 = Label(top, text="This is Header")
lbl1.pack()
lbl2 = Label(bottom, text="This is Bottom")
lbl2.pack()

# Message Box
# showerror, askquestion, askokcancel, askyesno, askretrycancel, showinfo
def funcnc():
    if var.get() == "":
        messagebox.showwarning(title="Warning")
    else:
        messagebox.askyesno(title="Exit", message="Do you want to exit?")  
        win.destroy()

var = StringVar()
txtIn = Entry(win, textvariable=var)
txtIn.place(x=10, y=450)

btn = Button(win, text="Info", command=funcnc)
btn.place(x=10,y= 490)

# List Box
def funci():
    lst.delete(ANCHOR)

lst = Listbox(win, width=30)
items = ["Apple","Banana","Orange","Cat"]

for i in items:
    lst.insert(END, i)

lst.pack()
btn = Button(win, text="Delete", command=funci).pack()


# Canvas
canvas = Canvas(win)
cord = 10,50,270,210
canvas.create_arc(cord, start = 0, extent =180, fill= "red")
canvas.create_line(cord)
canvas.pack()


# Toplevel
def funco():
    top.destroy()

top = Toplevel()
btn = Button(top, text="Close Window", command=funco).pack()    

# Progress Bar
def bar():
    for i in range(1,100):
        progress['value']= i
        progress.update_idletasks()
        time.sleep(0.01)

progress = ttk.Progressbar(win, orient=HORIZONTAL, length=100,
                           mode= "determinate")
                                 #indeterminate
progress.pack()
btn = Button(win, text="Start", command= bar).pack()


# Scrollbar
scroll = Scrollbar(win)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=win)

# Menu
def demo():
    pass

my_menu = Menu(win)
win.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label= "New", command= demo)
file_menu.add_separator()
file_menu.add_cascade(label= "Open", command= demo)

# Treeview
def opencsv():
    global name
    name = filedialog.askopenfilename(parent= win, initialdir= os.getcwd(),
                title= "Please select file:")
    filebtn.configure(text=name)
    with open(name) as f:
        reader = csv.DictReader(f, delimiter=',')
        for now in reader:
            mobile = now['Mobile Number']
            tree.insert("",0, values=(mobile))

scrollbarx = Scrollbar(win, orient=HORIZONTAL)
scrollbary = Scrollbar(win, orient= VERTICAL)

tree = ttk.Treeview(win, columns=("Mobile Number", "Status"), height=20,
                    selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

scrollbarx.config(command=tree.xview)
scrollbarx.pack(side= RIGHT, fill= X)


scrollbary.config(command=tree.yview)
scrollbary.pack(side= RIGHT, fill= Y)

tree.heading("Mobile Number", text= "Mobile Number", anchor=W)
tree.heading("Status", text= "Status", anchor=W)

tree.column('#1', stretch = NO, minwidth= 0, width=150)
tree.column('#2', stretch = NO, minwidth= 0, width=150)
tree.pack()

filebtn = Button(win, text= "Select CSV File", width="37",
                 font="Verdana 13 bold", command=opencsv)
filebtn.pack()


# Imageview

image = PhotoImage(file='hello.PNG')
lbl = Label(win, image=image)
lbl.pack()


win.mainloop()
 