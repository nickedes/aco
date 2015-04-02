# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 18:33:43 2015
"""


""" Differential probability of an SBox. """
def differential_probability(sbox):
    """
    Generate a difference distribution table.
    http://xsnippet.org/205001/
    www.iacr.org/conferences/eurocrypt2013/rump/104.pdf
    """
    size = len(sbox)
    # Create an empty matrix
    ddt = []
    for i in range(size):
        ddt.append([0] * size)
    
    for x in range(size):
        for y in range(size):
            if x == y:
                continue
            ddt[x ^ y][sbox[x] ^ sbox[y]] += 1

    # The top-left value is always 16
    # and is ignored during the analysis.
    ddt[0][0] = 0
    return ddt
    # Find maximum of the matrix
    # return max([max(row) for row in ddt])
    # return max([max(row) for row in ddt])