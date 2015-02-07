# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 23:11:38 2015

This is the phase 2 file that invloves converting the initially
generated sbox to a tsp problem.
The initial sbox will be converted to an edge matrix. The weights
between the nodes will be based on the maximum differential probablity value
of that node in relation to other nodes in the adjacency matrix.
"""

def create_matrix(sbox):
    size = len(sbox)    
    mat = []
    for i in range(size):
        mat.append([0] * size)    
    for x in range(size):
        for y in range(size):
            mat[x ^ y][sbox[x] ^ sbox[y]] += 1
    
    mat[0][0] = 0
    print(mat)