# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:39:06 2019

@author: Sadiq
"""

s=[]
mid=[]
array=[]
import matplotlib.pyplot as plt
import time
from time import clock
import random

def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergesort(R)
        mergesort(L)
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
            
            
        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1
            
        while j < len(R):
            array[k] = R[j]
            j+=1
            k+=1
            
            
            
if __name__=='__main__':
    for N in range(6000,20000,2000):
        for j in range(0,N):
            array.append(random.randint(1,6000))
        start=clock()
        mergesort(array)
        end=clock()
        time2=end-start
        mid.append(N)
        s.append(time2)
    plt.plot(mid,s)
    plt.grid()
    plt.show
    print("sadiq's code")
        
            