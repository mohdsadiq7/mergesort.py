# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:25:57 2019

@author: Sadiq
"""


s1=[]
mid=[]
s2=[]
n2=[]
s3=[]
n3=[]
s4=[]
n4=[]
s5=[]
n5=[]
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
       
       
def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[i]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        
        
        
def selectionsort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
                
        array[i],array[min_idx] = array[min_idx],array[i]    



if __name__=='__main__':
    for N in range(10,200,20):
        for j in range(0,N):
            array.append(random.randint(1,1000))
        start1=clock()
        mergesort(array)
        end1=clock()

        start2=clock()
        heapSort(array)
        end2=clock()
        
        start3=clock()
        quick(0,N-1)
        end3=clock()
        
        start4=clock()
        insertionsort(array)
        end4=clock()
       
        start5=clock()
        selectionsort(array)
        end5=clock()
       
        time1=end1-start1
        time2=end2-start2 
        time3=end3-start3 
        time4=end4-start4 
        time5=end5-start5
        mid.append(N)
        s1.append(time1)
        n2.append(N)
        s2.append(time2)
        n3.append(N)
        s3.append(time3)
        n4.append(N)
        s4.append(time4)  
        n5.append(N)
        s5.append(time5) 
        
    plt.plot(mid,s1,'red',label='merge')
    plt.plot(n2,s2,'blue',label='heap')
    plt.plot(n3,s3,'green',label='quick')
    plt.plot(n4,s4,'pink',label='insertion')
    plt.plot(n5,s5,'orange',label='selection')
    plt.legend(loc='best')
    plt.xlabel("input size")
    plt.ylabel("time taken")
    plt.scatter(mid,s1)
    plt.scatter(n2,s2)
    plt.scatter(n3,s3)
    plt.scatter(n4,s4)
    plt.scatter(n5,s5)
    plt.grid()
    plt.show()
    
        
