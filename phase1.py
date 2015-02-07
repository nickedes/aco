# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.999
# b  = 0.499


from decimal import *
from math import floor
from functions import *
from performance import *

def generate_sbox(num,den):
    # Set precision to 20
    getcontext().prec = 15

    # Define intital/constant values
    x = Decimal(num)/Decimal(den)
    u  = Decimal(3999)/Decimal(1000)
    b = Decimal(4999)/Decimal(10000)
    #print(x,u,b)
    # To counter Transient Effect
    # Iterate over Chaotic Logistic Map
    x = chaotic(x, u, 50)
    #print(x)

    # Iterate over Tent Map
    x = tent(x, b, 50)
    #print(x)

    # Generate S Box
    s = []
    while len(s) < 256:
        x = chaotic(x, u, 24) #25
        x = tent(x, b, 14) #14 
        #n = int(floor(256*x))
        n = int((float(x*(10**6)) - floor(x*(10**6)))*256)
        if n not in s:
            #print(len(s))
            #print(s)
            s.append(n)
    return s


if __name__ == '__main__':
    num = 15961
    den = 29589
    nn = []
    nume = []
    deno = []
    x_num=50
    x_den=10
    m=10
    n=10
    for i in range(4):
        print(i)
        for x in range(50):
            s = generate_sbox(num,den)    
            #print(pretty(s))
            #print(is_bijective(s))
            #print(differential_probability(s))
            nn.append(nonlinearity(s))
            nume.append(num)
            deno.append(den)
            num = num + x_num
            den = den - x_den
        x_num = x_num-m
        x_den = x_den+n  
    max_non=max(nn)
    print(max_non)
    index=nn.index(max_non)
    print(index)
    print(nume[index])
    print(deno[index])