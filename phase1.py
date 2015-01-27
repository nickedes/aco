# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.99
# b  = 0.49


from decimal import *
from random import randint
from math import floor
from functions import *
from performance import *

# Set precision to 20
getcontext().prec = 20

# Define intital/constant values
x = Decimal(15961)/Decimal(29589)
u  = Decimal(39999999999999999999)/Decimal(10000000000000000000)
b = Decimal(4999999999999999999)/Decimal(10000000000000000000)

print x
print u
print b

# To counter Transient Effect
# Iterate over Chaotic Logistic Map
x = chaotic(x, u, 50)
print x

# Iterate over Tent Map
x = tent(x, b, 50)
print x

# Generate S Box
s = []
while len(s) < 256:
    x = chaotic(x, u, 25)
    x = tent(x, b, 14)
    n = int(floor(256*x))
    if n not in s:
        # print len(s)
        # print s
        s.append(n)
    
print pretty(s)

print is_bijective(s) 

print nonlinearity(s)
