# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:22:06 2020

@author: Henri
"""

import random
import numpy
import math
import pylab
from mpl_toolkits.mplot3d import Axes3D

#graphe en 3D avec retours à zéro en histogramme
def graphe3D(m,n):
    zeros=[]
    fig = pylab.figure()
    ax = fig.gca(projection='3d')
    for j in range  (m):
        a=[0,0,0]
        x = numpy.zeros(n)
        y = numpy.zeros(n)
        z = numpy.zeros(n)
        dernieri=0
        for i in range (n):
            alea0 = random.choice([0,1,2])
            alea1 = random.choice([-1,1])
            if alea0==0:
                x[i] = x[i - 1] + alea1
                y[i] = y[i - 1]
                z[i] = z[i - 1]
                a[0]=a[0]+alea1
            elif alea0==1:
                x[i] = x[i - 1] 
                y[i] = y[i - 1] + alea1
                z[i] = z[i - 1]
                a[1]=a[1]+alea1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1]
                z[i] = z[i - 1] + alea1
                a[2]=a[2]+alea1
            if (math.fabs(a[0])+math.fabs(a[1])+math.fabs(a[2]))==0:
                    zeros.append(i-dernieri)
                    dernieri=i
                           
        ax.plot(x, y, z)
    
    pylab.title("Marche Aleatoire ($n = " + str(n) + "$ pas)")
    pylab.savefig('exercice5graphe.png')
    pylab.show()
    pylab.clf()

    pylab.hist(zeros, range = (0, max(zeros)), bins = n, color = 'blue',edgecolor = 'black')
    pylab.savefig('exercice5histo.png')
    pylab.clf()

