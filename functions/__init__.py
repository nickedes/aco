# Iterate over Chaotic Logistic Map
def chaotic(x, u, count):
    """ Iterates over the chaotic logistic map """

    for i in range(count):
        x = u*x*(1-x)
    return x

# Iterate over Tent Map
def tent(x, b, count):
    for i in range(count):
        if 0 < x and x <= b:
            x = x/b
        elif b < x and x < 1:
            x = (1-x)/(1-b)
        else:
            print "Something wrong at Tent Map"
    return x

