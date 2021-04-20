# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:20:55 2020

@author: Henri
"""

import random
import numpy
import pylab
import math as math

#graphe en 2D avec retours a zero en histogramme
def graphe2D(m,n):
    zeros=[]
    for j in range (m):
        a=[0,0]
        x = numpy.zeros(n)
        y = numpy.zeros(n)
        dernieri=0
        for i in range (n):
            alea1=random.choice([-1,1])
            if random.choice([0,1])==0:
                x[i] = x[i - 1] + alea1
                y[i] = y[i - 1]
                a[0]=a[0]+alea1
            else:
                x[i] = x[i - 1] 
                y[i] = y[i - 1] + alea1
                a[1]=a[1]+alea1
            if (math.fabs(a[0])+math.fabs(a[1]))==0:
                zeros.append(i-dernieri)
                dernieri=i
        pylab.plot(x, y)
    
    pylab.title("Marche Aleatoire ($n = " + str(n) + "$ pas)")
    
    pylab.savefig('exercice4graphe.png')
    pylab.clf()
    pylab.title("Temps des retours en zero: ")
    pylab.hist(zeros, range = (0, max(zeros)), bins = n, color = 'blue',edgecolor = 'black')
    pylab.savefig('exercice4histo.png')
    pylab.clf()

