# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 01:52:41 2019

@author: Sadiq
"""

n=[]
array=[]
s=[]
import matplotlib.pyplot as plt
import time
from time import clock
import random

def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[i]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        
if __name__=='__main__':
    for N in range(10000,100000,10000):
        for j in range(0,N):
            array.append(random.randint(1,20000))
        start=clock()
        insertionsort(array)
        end=clock()
        time2=end-start
        n.append(N)
        s.append(time2)
    plt.plot(n,s)
    plt.grid()
    plt.show
    print("sadiq's code")               
        