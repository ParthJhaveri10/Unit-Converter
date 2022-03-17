#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Conversion factors
unit_dict = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams": 1.0,
    "kg": 1000.0,
    "quintals": 100000.0,
    "tonnes": 1000000.0,
    "pounds": 453.592,
    "sq. m": 1.0,
    "sq. km": 1000000.0,
    "are": 100.0,
    "hectare": 10000.0,
    "acre": 4046.856,
    "sq. mile": 2590000.0,
    "sq. foot": 0.0929,
    "cu. cm": 0.001,
    "Litre": 1.0,
    "ml": 0.001,
    "gallon": 3.785,
    "hours": 3600,
    "miniutes":60,
    "seconds": 1
}

lengths = ["cm", "m", "km", "feet", "miles", "inches", ]
weights = ["kg", "grams", "quintals", "tonnes", "pounds", ]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]
times = ["hours", "miniutes", "seconds"]

OPTIONS = ["select units",
           "cm",
           "m",
           "km",
           "feet",
           "miles",
           "inches",
           "kg",
           "grams",
           "quintals",
           "tonnes",
           "pounds",
           "Celsius",
           "Fahrenheit",
           "sq. m",
           "sq. km",
           "are",
           "hectare",
           "acre",
           "sq. mile",
           "sq. foot",
           "cu. cm",
           "Litre",
           "ml",
           "gallon",
           "hours",
          "miniutes",
          "seconds"]

# CREATE A ROOT

root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x600")
root.resizable(False, False)
root["bg"] = "#13c258"

# Title label
title_label = Label(root, text='Welcome to Unit Converter', bg="#d5eef0")
title_label["font"] = ("Calibri", 20)
title_label.place(x=180, y=10)

# TAB COLOUR

s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L', '15'))

tabControl = ttk.Notebook(root)

tab1 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)
tab2 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)
tab3 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)
tab4 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)
tab5 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)
tab6 = tk.Frame(tabControl, bg="#13c258", width=200, height=200)

tabControl.add(tab1, text='Length')
tabControl.add(tab2, text='Temperature')
tabControl.add(tab3, text='Area')
tabControl.add(tab4, text='Volume')
tabControl.add(tab5, text='Weight')
tabControl.add(tab6, text='Time')
tabControl.pack(expand=1, fill="both")


def ok(tab):
    if tab == 1:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry.delete(0, END)
                outputentry.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

    elif tab == 2:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry2.get())
        print(inp)
        inp_unit = inputopt.get()
        print(inp_unit)
        out_unit = outputopt.get()
        print(out_unit)

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry2.delete(0, END)
                outputentry2.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry2.delete(0, END)
                outputentry2.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry2.delete(0, END)
                outputentry2.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry2.delete(0, END)
            outputentry2.insert(0, "ERROR")


    elif tab == 3:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry3.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry3.delete(0, END)
                outputentry3.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry3.delete(0, END)
                outputentry3.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry3.delete(0, END)
                outputentry3.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry3.delete(0, END)
            outputentry3.insert(0, "ERROR")

    elif tab == 4:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry4.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry4.delete(0, END)
                outputentry4.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry4.delete(0, END)
                outputentry4.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry4.delete(0, END)
                outputentry4.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry4.delete(0, END)
            outputentry4.insert(0, "ERROR")


    elif tab == 5:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry5.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry5.delete(0, END)
                outputentry5.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry5.delete(0, END)
                outputentry5.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry5.delete(0, END)
                outputentry5.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry5.delete(0, END)
            outputentry5.insert(0, "ERROR")
            
    elif tab == 6:
        if inputentry.get() == "":  
             messagebox.showerror("Empty Tabs", "DONT LEAVE EMPTY")
             return

        inp = float(inputentry6.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
                inp_unit in weights and out_unit in weights,
                inp_unit in temps and out_unit in temps,
                inp_unit in areas and out_unit in areas,
                inp_unit in volumes and out_unit in volumes,
                inp_unit in times and out_unit in times]

        if any(cons):  # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry6.delete(0, END)
                outputentry6.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry6.delete(0, END)
                outputentry6.insert(0, (inp - 32) * (5 / 9))
            else:
                outputentry6.delete(0, END)
                outputentry6.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

        else:  # Display error if units are of different types
            outputentry6.delete(0, END)
            outputentry6.insert(0, "ERROR")



inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])

# TAB 1

# Options for drop-down menu
OPTIONS1 = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches"]

inputlabel = Label(tab1, text="Input", width=20, bg="#f104df")
inputlabel.grid(row=0, column=0, pady=20)
inputlabel["font"] = (18)

inputentry = Entry(tab1, justify="center", font="bold")
inputentry.grid(row=1, column=0, padx=35, ipady=5)

inputmenu = OptionMenu(tab1, inputopt, *OPTIONS1)
inputmenu.grid(row=1, column=1)
inputmenu.config(font="Arial 10")

outputlabel = Label(tab1, text="Output", width=20, bg="#f104df")
outputlabel.grid(row=2, column=0, pady=20)
outputlabel["font"] = (18)

outputentry = Entry(tab1, justify="center", font="bold")
outputentry.grid(row=3, column=0, padx=35, ipady=5)

outputmenu = OptionMenu(tab1, outputopt, *OPTIONS1)
outputmenu.grid(row=3, column=1)
outputmenu.config(font="Arial 10")

convertbtn = Button(tab1, text="Convert", command=lambda: ok(1), padx=80, pady=2)
convertbtn.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn["bg"] = "orange"
convertbtn["fg"] = "black"

# TAB 2

OPTIONS2 = ["select units",
            "Celsius",
            "Fahrenheit"]

inputlabel2 = Label(tab2, text="Input", width=20, bg="#f104df")
inputlabel2.grid(row=0, column=0, pady=20)
inputlabel2["font"] = (18)

inputentry2 = Entry(tab2, justify="center", font="bold")
inputentry2.grid(row=1, column=0, padx=35, ipady=5)

inputmenu2 = OptionMenu(tab2, inputopt, *OPTIONS2)
inputmenu2.grid(row=1, column=1)
inputmenu2.config(font="Arial 10")

outputlabel2 = Label(tab2, text="Output", width=20, bg="#f104df")
outputlabel2.grid(row=2, column=0, pady=20)
outputlabel2["font"] = (18)

outputentry2 = Entry(tab2, justify="center", font="bold")
outputentry2.grid(row=3, column=0, padx=35, ipady=5)

outputmenu2 = OptionMenu(tab2, outputopt, *OPTIONS2)
outputmenu2.grid(row=3, column=1)
outputmenu2.config(font="Arial 10")

convertbtn2 = Button(tab2, text="Convert", command=lambda: ok(2), padx=80, pady=2)
convertbtn2.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn2["bg"] = "orange"
convertbtn2["fg"] = "black"

# TAB3


OPTIONS3 = ["select units",
            "sq. m",
            "sq. km",
            "are",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot"]

inputlabel3 = Label(tab3, text="Input", width=20, bg="#f104df")
inputlabel3.grid(row=0, column=0, pady=20)
inputlabel3["font"] = (18)

inputentry3 = Entry(tab3, justify="center", font="bold")
inputentry3.grid(row=1, column=0, padx=35, ipady=5)

inputmenu3 = OptionMenu(tab3, inputopt, *OPTIONS3)
inputmenu3.grid(row=1, column=1)
inputmenu3.config(font="Arial 10")

outputlabel3 = Label(tab3, text="Output", width=20, bg="#f104df")
outputlabel3.grid(row=2, column=0, pady=20)
outputlabel3["font"] = (18)

outputentry3 = Entry(tab3, justify="center", font="bold")
outputentry3.grid(row=3, column=0, padx=35, ipady=5)

outputmenu3 = OptionMenu(tab3, outputopt, *OPTIONS3)
outputmenu3.grid(row=3, column=1)
outputmenu3.config(font="Arial 10")

convertbtn3 = Button(tab3, text="Convert", command=lambda: ok(3), padx=80, pady=2)
convertbtn3.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn3["bg"] = "orange"
convertbtn3["fg"] = "black"

# TAB4

OPTIONS4 = ["select units",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]

inputlabel4 = Label(tab4, text="Input", width=20, bg="#f104df")
inputlabel4.grid(row=0, column=0, pady=20)
inputlabel4["font"] = (18)

inputentry4 = Entry(tab4, justify="center", font="bold")
inputentry4.grid(row=1, column=0, padx=35, ipady=5)

inputmenu4 = OptionMenu(tab4, inputopt, *OPTIONS4)
inputmenu4.grid(row=1, column=1)
inputmenu4.config(font="Arial 10")

outputlabel4 = Label(tab4, text="Output", width=20, bg="#f104df")
outputlabel4.grid(row=2, column=0, pady=20)
outputlabel4["font"] = (18)

outputentry4 = Entry(tab4, justify="center", font="bold")
outputentry4.grid(row=3, column=0, padx=35, ipady=5)

outputmenu4 = OptionMenu(tab4, outputopt, *OPTIONS4)
outputmenu4.grid(row=3, column=1)
outputmenu4.config(font="Arial 10")

convertbtn4 = Button(tab4, text="Convert", command=lambda: ok(4), padx=80, pady=2)
convertbtn4.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn4["bg"] = "orange"
convertbtn4["fg"] = "black"

# TAB5


OPTIONS5 = ["select units",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds"]

inputlabel5 = Label(tab5, text="Input", width=20, bg="#f104df")
inputlabel5.grid(row=0, column=0, pady=20)
inputlabel5["font"] = (18)

inputentry5 = Entry(tab5, justify="center", font="bold")
inputentry5.grid(row=1, column=0, padx=35, ipady=5)

inputmenu5 = OptionMenu(tab5, inputopt, *OPTIONS5)
inputmenu5.grid(row=1, column=1)
inputmenu5.config(font="Arial 10")

outputlabel5 = Label(tab5, text="Output", width=20, bg="#f104df")
outputlabel5.grid(row=2, column=0, pady=20)
outputlabel5["font"] = (18)

outputentry5 = Entry(tab5, justify="center", font="bold")
outputentry5.grid(row=3, column=0, padx=35, ipady=5)

outputmenu5 = OptionMenu(tab5, outputopt, *OPTIONS5)
outputmenu5.grid(row=3, column=1)
outputmenu5.config(font="Arial 10")

convertbtn5 = Button(tab5, text="Convert", command=lambda: ok(5), padx=80, pady=2)
convertbtn5.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn5["bg"] = "orange"
convertbtn5["fg"] = "black"

# Button for closing|
exit_button = Button(root, text="Exit",width = 20,font = (20), command=root.destroy)
exit_button.pack(pady=10)
exit_button["bg"] = "#13c258"
exit_button["fg"] = "black"

# TAB6


OPTIONS6 = ["select units",
           "hours",
          "miniutes",
          "seconds"]


inputlabel6 = Label(tab6, text="Input", width=20, bg="#f104df")
inputlabel6.grid(row=0, column=0, pady=20)
inputlabel6["font"] = (18)

inputentry6 = Entry(tab6, justify="center", font="bold")
inputentry6.grid(row=1, column=0, padx=35, ipady=5)

inputmenu6 = OptionMenu(tab6, inputopt, *OPTIONS6)
inputmenu6.grid(row=1, column=1)
inputmenu6.config(font="Arial 10")

outputlabel6 = Label(tab6, text="Output", width=20, bg="#f104df")
outputlabel6.grid(row=2, column=0, pady=20)
outputlabel6["font"] = (18)

outputentry6 = Entry(tab6, justify="center", font="bold")
outputentry6.grid(row=3, column=0, padx=35, ipady=5)

outputmenu6 = OptionMenu(tab6, outputopt, *OPTIONS6)
outputmenu6.grid(row=3, column=1)
outputmenu6.config(font="Arial 10")

convertbtn6 = Button(tab6, text="Convert", command=lambda: ok(6), padx=80, pady=2)
convertbtn6.grid(row=4, column=0, columnspan=1, pady=50)
convertbtn6["bg"] = "orange"
convertbtn6["fg"] = "black"



root.mainloop()


# 
