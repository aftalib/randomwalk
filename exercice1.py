# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:08:42 2020

@author: Henri
"""

import random
import matplotlib.pyplot as plt

#graphe en 1D avec minimum et maximum
def grapheExtremum():

    a=0
    n=1000
    x=list(range(0,n))
    y=[]
    for i in range (0,n):
        a=a+random.choice([-1,1])  
        y.append(a) 
    plt.title("Marche Aleatoire: p=0.5, n=1000")
    plt.plot(x,y)  
    plt.savefig('exercice1graphe.png')
    plt.clf()
    return "Valeur maximale: "+str(max(y))+"\n"+"Valeur minimale: "+str(min(y))+"\n"+"Valeur Finale: "+str(a)

#graphe en 1D avec valeurs en entrée
def graphe1D(m,n):
    
    x=list(range(0,n))
    for j in range (m):
        a=0
        y=[]
        for i in range (0,n):
           a=a+random.choice([-1,1])  
           y.append(a) 
        plt.plot(x,y)  
           
    plt.title("Marche Aleatoire ($n = " + str(n) + "$ pas)")
    plt.savefig('exercice1graphe2.png')
    plt.clf()
