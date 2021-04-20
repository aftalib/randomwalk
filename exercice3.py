# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:19:56 2020

@author: Henri
"""
import random
import matplotlib.pyplot as plt

#graphe en 1D avec retours à zero en histogramme
def grapheretourzero():
    m=100
    n=10000
    
    zeros=[] #gardera les retours a zero
    x=list(range(0,n))
    for j in range(m):
        a=0
        dernieri=0 #garde l'emplaement du dernier retour a zero
        y=[]
        for i in range (0,n):
            a=a+random.choice([-1,1,1,1])
            y.append(a)  
            if a==0:
                zeros.append(i-dernieri)
                dernieri=i
        plt.plot(x,y)
        
    plt.title("100 Marche Aleatoire: p=0.75, n=10000")
    plt.savefig('exercice3graphe.png')
    plt.clf()
    plt.title("Temps des retours en zero: ")
    plt.hist(zeros, range = (0, max(zeros)), bins = n, color = 'blue',edgecolor = 'black')
    plt.savefig('exercice3histo.png')
    plt.clf()