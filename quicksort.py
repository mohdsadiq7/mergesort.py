# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 01:39:11 2019

@author: Sadiq
"""

n=[]
array=[]
s=[]
import matplotlib.pyplot as plt
import time
from time import clock
import random


def partition(low,high):
    i=low-1
    temp=array[high]
    for j in range(low,high):
        if(array[j]<=temp):
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)

def quick(low,high):
    if(low<high):
       pi=partition(low,high)
       quick(low,pi-1)
       quick(pi+1,high)
       
       
if __name__=='__main__':
    for N in range(10000,100000,10000):
        for j in range(0,N):
            array.append(random.randint(1,10000))
        start=clock()
        quick(0,N-1)
        end=clock()
        time2=end-start
        n.append(N)
        s.append(time2)
    plt.plot(n,s)
    plt.grid()
    plt.show
    print("sadiq's code")       