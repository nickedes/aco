# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:53:01 2015
"""
from scipy.linalg import hadamard

def bitlist(val):
    """returns a list of the bits after conversion into binary."""
    bitlst = [int(bit) for bit in bin(val)[2:]]
    leng = 8
    while len(bitlst) < leng:
        bitlst.insert(0, 0)
    return bitlst

def nonlinearity(box):
    rows = 256  #256
    cols = 8   #8
    boolarr = [[0]*8 for i in range(256)]   
    
    for hh in range(rows):
        for jj in range(cols):
            boolarr[hh][cols-jj-1]  = (-1)**(bitlist(box[hh])[-(jj+1)])
            
#    print(boolarr)
    h = hadamard(rows)
    asum = 0
    nn = [0*i for i in range(cols)]
    count = 0
    
    for hh in range(cols):
        maximum = 0
        for kk in range(rows):
            temp = 0
            for jj in range(rows):
                if boolarr[jj][hh] == h[kk][jj]:
                    temp += 1
                else:
                    temp -= 1
            temp = abs(temp)
            count += 1
            
            if temp > maximum:
                maximum = temp
        nn[cols - 1 - hh] = 128 - maximum/2
        asum = asum + nn[cols - 1 - hh]

    avg = asum/cols
    #print(nn)
    return avg