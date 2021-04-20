# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:51:14 2020

@author: Mehdi
"""

import tkinter
from tkinter import Entry
from tkinter import Toplevel
from PIL import ImageTk, Image

import exercice1
import exercice2
import exercice3
import exercice4
import exercice5

def ex1photo():
    #creer la fenetre
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x345")
    window.configure(background='grey')
    #creer le graphe, mettre les données dans la variable texte
    text=tkinter.Text(window)
    text.insert(tkinter.INSERT, exercice1.grapheExtremum())
    #prendre l'image du graphe
    img = ImageTk.PhotoImage(Image.open("exercice1graphe.png"))
    panel = tkinter.Label(window, image = img)
    #tout afficher
    panel.pack(side = "top", fill = "none", expand = "no")
    text.pack(side = "bottom", fill = "none", expand = "no")
    window.mainloop()
    
def ex1fenetre():
    #Generera un graphe qui sera affiché susr la fenêtre créée
    def ex1graphe():
        exercice1.graphe1D(m.get(),n.get())
        window2 = tkinter.Toplevel()
        window2.title("Graphe")
        window2.geometry("432x288")
        window2.configure(background='grey')
        img = ImageTk.PhotoImage(Image.open("exercice1graphe2.png"))
        panel = tkinter.Label(window2, image = img)
        panel.pack(side = "top", fill = "none", expand = "no")
        window2.mainloop()
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x288")
    #entree 1
    m = tkinter.IntVar()
    label = tkinter.Label(window,text="Nombre de marches m :")
    label.pack()
    name = tkinter.Entry(window, textvariable=m)
    name.focus_set()
    name.pack()
    #entree 2
    n = tkinter.IntVar()
    label2 = tkinter.Label(window,text="Nombre de pas n :")
    label2.pack()
    name2 = tkinter.Entry(window, textvariable=n)
    name2.focus_set()
    name2.pack()
    #bouton
    labelButton = tkinter.Label(window, text='')
    button = tkinter.Button(window, text='Lancer la simulation', command=ex1graphe)
    button.pack()
    window.mainloop()
    
def ex2photo1():
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x330")
    window.configure(background='grey')
    text=tkinter.Text(window)
    text.insert(tkinter.INSERT, exercice2.grapheComparaison())
    img = ImageTk.PhotoImage(Image.open("exercice2graphe1.png"))
    panel = tkinter.Label(window, image = img)
    panel.pack(side = "top", fill = "none", expand = "no")
    text.pack(side = "bottom", fill = "none", expand = "no")
    window.mainloop()

def ex2photo2():
    exercice2.graphe075()
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x288")
    window.configure(background='grey')
    img = ImageTk.PhotoImage(Image.open("exercice2graphe2.png"))
    panel = tkinter.Label(window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    window.mainloop()
    
def ex3photo():
    exercice3.grapheretourzero()
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x576")
    window.configure(background='grey')
    img = ImageTk.PhotoImage(Image.open("exercice3graphe.png"))
    panel = tkinter.Label(window, image = img)
    panel.pack(side = "top", fill = "none", expand = "no")
    img2 = ImageTk.PhotoImage(Image.open("exercice3histo.png"))
    panel = tkinter.Label(window, image = img2)
    panel.pack(side = "bottom", fill = "none", expand = "no")
    window.mainloop()
    

    
def ex4fenetre():
    def ex4graphe():
        exercice4.graphe2D(m.get(),n.get())
        window2 = tkinter.Toplevel()
        window2.title("Graphe")
        window2.geometry("432x576")
        window2.configure(background='grey')
        img = ImageTk.PhotoImage(Image.open("exercice4graphe.png"))
        panel = tkinter.Label(window2, image = img)
        panel.pack(side = "top", fill = "none", expand = "no")
        img2 = ImageTk.PhotoImage(Image.open("exercice4histo.png"))
        panel2 = tkinter.Label(window2, image = img2)
        panel2.pack(side = "bottom", fill = "none", expand = "no")
        window2.mainloop()
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x288")
    m = tkinter.IntVar()
    label = tkinter.Label(window,text="Nombre de marches m :")
    label.pack()
    name = tkinter.Entry(window, textvariable=m)
    name.focus_set()
    name.pack()
    n = tkinter.IntVar()
    label2 = tkinter.Label(window,text="Nombre de pas n :")
    label2.pack()
    name2 = tkinter.Entry(window, textvariable=n)
    name2.focus_set()
    name2.pack()
    labelButton = tkinter.Label(window, text='')
    button = tkinter.Button(window, text='Lancer la simulation', command=ex4graphe)
    button.pack()
    window.mainloop()

def ex5fenetre():
    def ex5graphe():
        exercice5.graphe3D(m.get(),n.get())
        window2 = tkinter.Toplevel()
        window2.title("Graphe")
        window2.geometry("432x576")
        window2.configure(background='grey')
        img = ImageTk.PhotoImage(Image.open("exercice5graphe.png"))
        panel = tkinter.Label(window2, image = img)
        panel.pack(side = "top", fill = "none", expand = "no")
        img2 = ImageTk.PhotoImage(Image.open("exercice5histo.png"))
        panel2 = tkinter.Label(window2, image = img2)
        panel2.pack(side = "bottom", fill = "none", expand = "no")
        window2.mainloop()
    window = tkinter.Toplevel()
    window.title("Graphe")
    window.geometry("432x288")
    m = tkinter.IntVar()
    label = tkinter.Label(window,text="Nombre de marches m :")
    label.pack()
    name = tkinter.Entry(window, textvariable=m)
    name.focus_set()
    name.pack()
    n = tkinter.IntVar()
    label2 = tkinter.Label(window,text="Nombre de pas n :")
    label2.pack()
    name2 = tkinter.Entry(window, textvariable=n)
    name2.focus_set()
    name2.pack()
    labelButton = tkinter.Label(window, text='')
    button = tkinter.Button(window, text='Lancer la simulation', command=ex5graphe)
    button.pack()
    window.mainloop()



app1 = tkinter.Tk()
app1.geometry("640x480")
app1.title("Menu Marche Aléatoire")

mainmenu = tkinter.Menu(app1)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Marche Extremum", command=ex1photo)
first_menu.add_command(label="Graphe 1D", command=ex1fenetre)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Marche Comparaison", command=ex2photo1)
second_menu.add_command(label="Graphe p=0.75", command=ex2photo2)

third_menu = tkinter.Menu(mainmenu, tearoff=0)
third_menu.add_command(label="Graphe retour zero", command=ex3photo)

fourth_menu = tkinter.Menu(mainmenu, tearoff=0)
fourth_menu.add_command(label="Graphe 2D", command=ex4fenetre)

fifth_menu = tkinter.Menu(mainmenu, tearoff=0)
fifth_menu.add_command(label="Graphe 3D", command=ex5fenetre)

mainmenu.add_cascade(label="Exercice 1", menu=first_menu)
mainmenu.add_cascade(label="Exercice 2", menu=second_menu)
mainmenu.add_cascade(label="Exercice 3", menu=third_menu)
mainmenu.add_cascade(label="Exercice 4", menu=fourth_menu)
mainmenu.add_cascade(label="Exercice 5", menu=fifth_menu)

w = Entry( app1)


app1.config(menu=mainmenu)
app1.mainloop()
