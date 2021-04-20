# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:12:33 2020

@author: Henri
"""

import random
import matplotlib.pyplot as plt

#graphe en 1D avec p=0.5 et p=0.75
def grapheComparaison():

    n=10000
    x=list(range(0,n))
    a=0
    b=0
    y=[]
    y2=[]
    
    for j in range (n):
        a=a+random.choice([-1,1,1,1])
        y.append(a) 
        
    for j in range (n):
        b=b+random.choice([-1,1])
        y2.append(b)
        
    plt.title("Marche Aleatoire: p=0.5 et p=.075, n=10000")
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.savefig('exercice2graphe1.png')
    plt.clf()
    return "Valeur finale pour p=0.5: "+str(b)+"\n"+"Valeur finale pour p=0.75: "+str(a)

#9graphe en 1D avec p=0.75
def graphe075():
    m=100
    n=10000
    x=list(range(0,n))
    for i in range (m): 
        a=0
        y=[]
        for j in range (n):
            a=a+random.choice([-1,1,1,1])
            y.append(a) 
        plt.plot(x,y)  
    plt.title("100 Marche Aleatoire: p=0.75, n=10000")
    plt.savefig('exercice2graphe2.png')
    plt.clf()
    
    

