from tkinter import * #start by importing tkinter
from tkinter import ttk
from tkinter import filedialog

def calculate(*args):#bags of coffee to cups of coffee calculation
    try:
        value = float(feet.get())
        meters.set(value*1.75)
    except ValueError:
        pass

def show_entry_fields():#show/print statements
    print(" ")
    print("coffee name:")
    print(e1.get())
    print("Number of coffee bags :")
    print(e2.get())
    print("Coffeemaker's statements :")
    print(e3.get())

def empty_row(col,row,color):#inserting empty rows
    namebox=Text(master,height=2,width=30,borderwidth=0,highlightthickness=0)
    namebox.grid(column=col,row=row)
    namebox.config(bg=color)
    return namebox

def empty_row2(col,row,color):#inserting empty rows
    namebox=Text(master,height=2,width=50,borderwidth=0,highlightthickness=0)
    namebox.grid(column=col,row=row)
    namebox.config(bg=color)
    return namebox

def test(event):
    print(event)

master = Tk()#master is the name of the widow
master.title(" COFFEE CALCULATOR")
root = Tk()

topframe = Frame(root,bg='blue',height='20')
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='20',width='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind("<Button-1>",test ) # keyword 
can1.pack(side=LEFT, padx=5, pady=5)


master.minsize(width=200, height=200)#size of window
master.geometry('585x550+0+0')

mycolor = '#%02x%02x%02x' % (237, 237, 140)#red, green, blue
master.configure(bg=mycolor)
mycolorr = '#%02x%02x%02x' % (169, 225, 245)#greeny blue
mycolorrr = '#%02x%02x%02x' % (186, 93, 22)#Brown
mycolorrrr = '#%02x%02x%02x' % (135, 69, 18)#Darker brown

#namebox1= empty_row2(1,5,mycolorr)#current existing empty rows
namebox2= empty_row(1,7,mycolorrrr)
namebox3= empty_row2(1,12,mycolorr)
#namebox4= empty_row2(0,5,mycolorr)
namebox5= empty_row(0,7,mycolorrr)
namebox6= empty_row(0,12,mycolorr)


Label(master, text="Now choose your coffee type!!").grid(row=5, column=1)
Label(master, text="Now choose your coffee type!!").grid(row=5, column=0)
Label(master, text="Welcome to coffee calculator!!").grid(row=0, column=1)
Label(master, text="Welcome to coffee calculator!!").grid(row=0, column=0)
Label(master, text="Name your Coffee :").grid(row=1)
Label(master, text="Number of bags of coffee :").grid(row=2)
Label(master, text="Personal statements :").grid(row=3)#labels

e1 = Entry(master)#entry feilds
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

Button(master, text='Show/Print', command=show_entry_fields).grid(row=4, column=1)
#This puts the print function into use

CheckVar1 = IntVar()#checkbox1
CheckVar2 = IntVar()#checkboc2
C1 = Checkbutton(master, text = "Americano coffee", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20, ).grid(row=6, column=0)
C2 = Checkbutton(master, text = "Frappuccino coffee", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20).grid(row=6, column=1)

Button(master, text='Quit', command=quit).grid(row=13, column=0)#To quit program
Button(master, text='Continue').grid(row=13, column=1)#To finish program

Label(master, text=" Now calculate the amount of coffee you can make!! ").grid(row=8, column=1)#label

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(master, width=7, textvariable=feet)#Input entrybox in calculation function
feet_entry.grid(column=1, row=9, sticky=(W, E))

ttk.Label(master, textvariable=meters).grid(column=1, row=10, sticky=(W, E))#show calculations
ttk.Button(master, text="Calculate", command=calculate).grid(column=1, row=11, sticky=W)#press to convert units and calculate

ttk.Label(master, text="bags of coffee(175g/bag)").grid(column=0, row=9, sticky=E)#labels
ttk.Label(master, text="cups of coffee can make").grid(column=0, row=10, sticky=E)

for child in master.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()#return calculations
master.bind('<Return>', calculate)
master.mainloop()
root.mainloop()
