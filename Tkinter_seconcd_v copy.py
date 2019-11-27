# start by importing tkinter
from tkinter import *
from tkinter import ttk

# master is the name of the widow
master = Tk()
master.title("COFFEE CALCULATOR")
root = Tk()


def calculate():
    """ Bags of coffee to cups of coffee calculation """
    try:
        value = float(feet.get())
        meters.set(value * 1.75)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


def show_entry_fields():
    """ Show/Print statements """
    print("coffee name: ", e1.get())
    print("Number of coffee bags: ", e2.get())
    print("Coffeemaker's statements: ", e3.get())


def empty_row(col, row, color):
    """ Inserte empty rows """
    if col < 0 or row < 0:
        raise Exception("Column or row cannot be negative.")
    namebox = Text(master, height=2, width=30, borderwidth=0, highlightthickness=0)
    namebox.grid(column=col, row=row)
    namebox.config(bg=color)
    return namebox


def setup_labels():
    """ Setup label for view """
    Label(master, text="Now choose your coffee type!!").grid(row=5, column=1)
    Label(master, text="Now choose your coffee type!!").grid(row=5, column=0)
    Label(master, text="Welcome to coffee calculator!!").grid(row=0, column=1)
    Label(master, text="Welcome to coffee calculator!!").grid(row=0, column=0)
    Label(master, text="Name your Coffee :").grid(row=1)
    Label(master, text="Number of bags of coffee :").grid(row=2)
    Label(master, text="Personal statements :").grid(row=3)


def return_calculations():
    """ Return calculations """
    feet_entry.focus()
    master.bind('<Return>', calculate)
    master.mainloop()
    root.mainloop()


def setup_empty_rows():
    """ Set up coloured empty rows """
    yellow_colour = '#%02x%02x%02x' % (237, 237, 140)
    green_blue_colour = '#%02x%02x%02x' % (169, 225, 245)
    brown_colour = '#%02x%02x%02x' % (186, 93, 22)
    dark_brown_colour = '#%02x%02x%02x' % (135, 69, 18)

    empty_row(1, 7, dark_brown_colour)
    empty_row(1, 12, green_blue_colour)
    empty_row(0, 7, brown_colour)
    empty_row(0, 12, green_blue_colour)

    master.configure(bg=yellow_colour)


def setup_buttons():
    """ Set up buttons """
    # This puts the print function into use
    Button(master, text='Show/Print', command=show_entry_fields).grid(row=4, column=1)
    # To quit program
    Button(master, text='Quit', command=quit).grid(row=13, column=0)
    # To finish program
    Button(master, text='Continue').grid(row=13, column=1)


while True:
    try:
        # size of window
        master.minsize(width=200, height=200)
        master.geometry('585x550+0+0')

        setup_empty_rows()
        setup_labels()
        setup_buttons()

        # checkboxes
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()

        C1 = Checkbutton(master, text="Americano coffee", variable=CheckVar1,\
                         onvalue=1, offvalue=0, height=2,\
                         width=20, ).grid(row=6, column=0)
        C2 = Checkbutton(master, text="Frappuccino coffee", variable=CheckVar2,\
                         onvalue=1, offvalue=0, height=2,\
                         width=20).grid(row=6, column=1)

        Label(master, text=" Now calculate the amount of coffee you can make!! ").grid(row=8, column=1)

        feet = StringVar()
        meters = StringVar()

        # setup_fields
        e1 = Entry(master)
        e2 = Entry(master)
        e3 = Entry(master)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)

        # Input entrybox in calculation function
        feet_entry = ttk.Entry(master, width=7, textvariable=feet)
        feet_entry.grid(column=1, row=9, sticky=(W, E))

        # show calculations
        ttk.Label(master, textvariable=meters).grid(column=1, row=10, sticky=(W, E))
        # press to convert units and calculate
        ttk.Button(master, text="Calculate", command=calculate).grid(column=1, row=11, sticky=W)

        ttk.Label(master, text="bags of coffee(175g/bag)").grid(column=0, row=9, sticky=E)
        ttk.Label(master, text="cups of coffee can make").grid(column=0, row=10, sticky=E)

        for child in master.winfo_children():
            child.grid_configure(padx=5, pady=5)

        return_calculations()

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except SyntaxError:
        print("Oops! Invalid syntax. Try again...")
