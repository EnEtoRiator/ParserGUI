from tkinter import *
from tkinter import ttk
import tkinter as tk
from dataParse import dataVars
#download tkinter! pip install tkinter
#imports are important! ;)
#descriptions are created for cynpy from EnEtoRiator.


#Create a tkinter window
window = Tk()


#declare a variables and give them tkinter.Entry() values
whatParse_var = tk.StringVar()
cityParse_var = tk.StringVar()
fileName_var = tk.StringVar()

#window settings function
def windowSettings():
    window.title("Parser")
    window.geometry("500x400")
    window.maxsize(500,400)
    window.minsize(500,400)
    window.resizable(height = None, width = None)
    window["bg"] = '#112D4E'
    window.iconbitmap('source/parser.ico')
def startParse():
    #declare a local variables and give them values from previous vars
    whatP = whatParse_var.get()
    cityP = cityParse_var.get()
    fileN = fileName_var.get()
    #update dictionary values from tkinter.Entry()
    dataVars.update({'Organisation' : whatP})
    dataVars.update({'City' : cityP})
    dataVars.update({'FileName' : fileN})

    #For check what we are have
    print(dataVars['Organisation'])
    print(dataVars['City'])
    print(dataVars['FileName'])

    #clear our variables
    whatParse_var.set("")
    cityParse_var.set("")
    fileName_var.set("")
    #checking the full dictionary
    print(dataVars)
#quit from program function
def quitt():
    window.quit()

#call function
windowSettings()

#frame for stylistics
Mainframe = Frame(window,bg='#393E46',bd=2,width=480,height=385).place(relx=0.02,rely=0.02)

#Organisation Text
whatParse_lbl = Label(Mainframe, text="Поиск :", width=26, height=2, font='Menlo 10', bg="#222831", fg="#EEEEEE").place(x=20,y=20)
#Organisation Entry
whatParse_entry = Entry(Mainframe, textvariable = whatParse_var, borderwidth=4,width=35) .place(x=250,y=30)

#City Text
cityParse_lbl = Label(Mainframe, text="В каком городе искать?", width=26, height=2, font='Menlo 10', bg="#222831", fg="#EEEEEE").place(x=20,y=120)
#Ciry Entry
cityParse_entry = Entry(Mainframe, textvariable = cityParse_var, borderwidth=4,width=35).place(x=250,y=130)

#File name Text
fileName_lbl = Label(Mainframe, text="Название файла с результатом:", width=26, height=2, font='Menlo 10', bg="#222831", fg="#EEEEEE").place(x=20,y=220)
#File name Entry
fileName_entry = Entry(Mainframe, textvariable = fileName_var, borderwidth=4,width=35).place(x=250,y=230)

#Button(Trigger) for startParse() function
startButton = Button(Mainframe, text="Искать!", command=startParse, width=10, height=2, font='Menlo 14', bg="#222831", fg="#EEEEEE").place(x=40,y=300)
#Button(Trigger) for quitt() function
deleteButton = Button(Mainframe, text="Выход", command=quitt, width=10, height=2, font='Menlo 14', bg="#222831", fg="#EEEEEE").place(x=340,y=300)
#cycle
window.mainloop()
