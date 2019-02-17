# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 01:58:54 2019

@author: Sadiq
"""

n=[]
array=[]
s=[]
import matplotlib.pyplot as plt
import time
from time import clock
import random


def selectionsort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
                
        array[i],array[min_idx] = array[min_idx],array[i]    


if __name__=='__main__':
    for N in range(1000,10000,1000):
        for j in range(0,N):
            array.append(random.randint(1,2000))
        start=clock()
        selectionsort(array)
        end=clock()
        time2=end-start
        n.append(N)
        s.append(time2)
    plt.plot(n,s)
    plt.grid()
    plt.show
    print("sadiq's code")         