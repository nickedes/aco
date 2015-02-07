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
        x = chaotic(x, u, 25) #25
        x = tent(x, b, 14) #14 
        #n = int(floor(256*x))
        n = int((float(x*(10**6)) - floor(x*(10**6)))*256)
        if n not in s:
            #print(len(s))
            #print(s)
            s.append(n)
    return s


if __name__ == '__main__':
#    s = generate_sbox()
    s = [86, 59, 119, 252, 213, 169, 132, 129, 159, 97, 223, 17, 190, 
         5, 236, 240, 95, 137, 134, 8, 148, 3, 7, 32, 205, 177, 62, 182, 
         211, 2, 255, 44, 107, 167, 224, 121, 244, 185, 18, 73, 109, 106,
         184, 124, 165, 99, 220, 77, 75, 154, 248, 215, 203, 108, 136, 90, 
         146, 38, 158, 208, 228, 151, 251, 171, 6, 249, 242, 246, 227, 74, 
         16, 12, 226, 128, 67, 133, 80, 209, 143, 178, 135, 229, 35, 180, 
         15, 254, 170, 112, 222, 19, 247, 84, 65, 48, 179, 142, 202, 13, 
         0, 105, 37, 200, 199, 27, 29, 234, 20, 216, 56, 197, 49, 191, 163, 
         245, 57, 110, 130, 24, 131, 79, 10, 91, 193, 149, 206, 204, 1, 172, 
         23, 36, 116, 156, 155, 175, 71, 89, 102, 139, 160, 82, 152, 187, 4, 
         85, 98, 21, 153, 87, 31, 54, 40, 144, 100, 101, 69, 225, 150, 53, 
         51, 210, 195, 30, 250, 239, 219, 9, 46, 192, 81, 55, 162, 33, 212, 
         42, 127, 93, 168, 114, 120, 243, 164, 138, 28, 166, 214, 25, 11, 
         235, 92, 122, 201, 238, 232, 66, 26, 125, 60, 231, 115, 72, 96, 61,
         140, 123, 50, 58, 221, 183, 161, 237, 22, 196, 189, 118, 68, 113, 
         70, 78, 104, 63, 145, 83, 34, 181, 43, 45, 41, 126, 233, 230, 76, 
         176, 88, 141, 198, 94, 117, 64, 207, 186, 52, 14, 39, 157, 218, 
         111, 253, 103, 217, 173, 188, 147, 174, 194, 47, 241]
    
    for i in range(256):
        if s[i] == 20: print("20 -> %d" % i)
    print(pretty(s))
    print(is_bijective(s))
#    nonlinearity(s)
    print(differential_probability(s))