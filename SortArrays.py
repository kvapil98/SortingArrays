# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:48:00 2018

@author: kvapil98
"""

#This algorithm sorts 2 sorted arrays and sorts them in a new array 

#initialized arrays for a simplified example
a = [1,9,57]
b = [7,15,45]
c = [0,0,0,0,0,0]

#intializes indices for the arrays
i = len(a) - 1
j = len(b) - 1
k = len(a)+len(b) - 1

#simultaneously keeps track of both independant arrays
while i>=0 or j>=0:
    
    #breaks if combined array is full
    if k<0:
        break
    
    #accounts for index i reaching -1
    if i<0:
        i=0
        if b[j]<=a[i]: #accounts for if a[0] is bigger so the oppiste would happen because a[0] is already accounted for
            c[k] = b[j]
            j-=1
            i-=1
            k-=1
            continue
    
    #accounts for index j reaching -1
    if j<0:
        j=0
        if a[i]<=b[j]: #accounts for if b[0] is bigger so the oppiste would happen because b[0] is already accounted for
            c[k] = a[i]
            j-=1
            i-=1
            k-=1
            continue
    
    #actual sorting mechanic where the bigger number is inserted
    if a[i] >= b[j]:
        c[k] = a[i]
        i-=1
        k-=1
    else:
        c[k] = b[j]
        j-=1
        k-=1
    

print(c) #print statement easy for testing