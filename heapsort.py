# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 01:01:50 2019

@author: Sadiq
"""
n=[]
array=[]
s=[]
import matplotlib.pyplot as plt
import time
from time import clock
import random

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l <n and array[i] < array[l]:
        largest = 1
        
    if r < n and array[largest] < array[r]:
        largest = 1
        
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
        
    for i in range(n-1, 0, -1):
        array[i],array[0] = array[0],array[i]
        heapify(array, i, 0)


if __name__=='__main__':
    for N in range(1000,9000,1000):
        for j in range(0,N):
            array.append(random.randint(1,1000))
        start=clock()
        heapSort(array)
        end=clock()
        time2=end-start
        n.append(N)
        s.append(time2)
    plt.plot(n,s)
    plt.grid()
    plt.show
    print("sadiq's code")