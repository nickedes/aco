# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.999
# b  = 0.499


from decimal import *
from random import randint
from math import floor
from functions import *
from performance import *

def generate_sbox():
    # Set precision to 20
    getcontext().prec = 15

    # Define intital/constant values
    x = Decimal(15961)/Decimal(29589)
    u  = Decimal(3999)/Decimal(1000)
    b = Decimal(4999)/Decimal(10000)

    print(x)
    print(u)
    print(b)

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
##        t1 = int((float(x*(10**6)) - floor(x*(10**6)))*25)
##        t2 = int((float(x*(10**6)) - floor(x*(10**6)))*14)
        x = chaotic(x, u, 25)
        x = tent(x, b, 14)
        #n = int(floor(256*x))
        n = int((float(x*(10**6)) - floor(x*(10**6)))*256)
        if n not in s:
            #print(len(s))
            #print(s)
            s.append(n)
    return s


#if __name__ == '__main__':
#    s = generate_sbox()
#    print(pretty(s))
#    print(is_bijective(s))


print((nonlinearity(s)))
#s = test_nonlinearity(s)
#x=0
#print(s)
#for i in s:
#    x += i
#    
#x /= len(s)
#print("Non linearity: {}" . format(x))
