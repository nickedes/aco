# Iterate over Chaotic Logistic Map
def chaotic(x, u, count):
    """ Iterate over the chaotic logistic map """

    for i in range(count):
        x = u*x*(1-x)
    return x

# Iterate over Tent Map
def tent(x, b, count):
    """ Iterate over the tent map """
    for i in range(count):
        if 0 < x and x <= b:
            x = x/b
        elif b < x and x < 1:
            x = (1-x)/(1-b)
        else:
            print("Something wrong at Tent Map")
    return x


def pretty(sbox):
    """ Return a pretty printed SBox """

    # List of Columns
    p = '\n       '
    for i in range(16):
        p += '%03d' % i + '  '
    p += '\n'

    for i in range(85):
        p += '-'
    

    # Pretty Values
    k=0    
    for i in range(256):
        if i%16 == 0:
            p += '\n%02d' % k + '  |  '
            k += 1
        p += '%03d' % sbox[i] + '  '
    
    return p.upper()