# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.999
# b  = 0.499

import operator
from decimal import *
from math import floor
from functions import *
from performance import *


def generate_sbox():
    # Set precision to 15
    getcontext().prec = 15

    # Define intital/constant values
    num = 20821
    den = 27729
    x = Decimal(num) / Decimal(den)
    u = Decimal(3999) / Decimal(1000)
    b = Decimal(4999) / Decimal(10000)
    print(x, u, b)
    # To counter Transient Effect
    # Iterate over Chaotic Logistic Map
    x = chaotic(x, u, 50)
    # print(x)

    # Iterate over Tent Map
    x = tent(x, b, 50)
    # print(x)

    # Generate S Box
    s = []
    while len(s) < 256:
        x = chaotic(x, u, 24)  # 25
        x = tent(x, b, 14)  # 14
        #n = int(floor(256*x))
        n = int((float(x * (10 ** 6)) - floor(x * (10 ** 6))) * 256)
        if n not in s:
            # print(len(s))
            # print(s)
            s.append(n)
    return s

def swap(s,x,y):
    swape = s[x]
    s[x] = s[y]
    s[y] = swape
    return s
if __name__ == '__main__':
    nn = []
    s = generate_sbox()
    print(pretty(s))
    print(is_bijective(s))
    ddt = differential_probability(s)
    dp = max([max(row) for row in ddt])
    max_values_rows = [0]
    for i in range(len(ddt)):
        if dp in ddt[i]:
            max_values_rows.append(i)
    print(max_values_rows)

    min_vales = {}
    for i in range(1, len(ddt)):
        if i not in max_values_rows:
            # print(min(ddt[i]),"of row:",i," has occurences:",ddt[i].count(min(ddt[i])))
            min_vales[i] = ddt[i].count(min(ddt[i]))
    sorted_min_val =  sorted(min_vales.items(), key=operator.itemgetter(1))
    # print(sorted_min_val)
    lol = [(142, 162), (210, 162), (231, 162), (242, 162), (118, 163), (154, 163), (244, 163)]
    print(s[72],s[244])
    
    for i in range(1,len(sorted_min_val)):
        if i == len(max_values_rows):
            break
        else:    
            s = swap(s,sorted_min_val[len(sorted_min_val)-i][0], max_values_rows[i])
    print(pretty(s))
    ddt = differential_probability(s)
    dp = max([max(row) for row in ddt])
    print(dp)
    nn.append(nonlinearity(s))
    max_non = max(nn)
    print(max_non)
