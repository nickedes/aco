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
    """ Return a pretty printed SBox.
        This function is coded by Shadab Zafar
        Refer: https://github.com/dufferzafar/substitute/blob/master/core/__init__.py
    """

    # List of Columns
    p = '\n       '
    for i in range(16):
        p += '%02x' % i + '  '
    p += '\n'

    for i in range(70):
        p += '-'
    p += '\n'

    # Row
    for i in range(16):
        p += '%02x' % i + '  |  '

        # Entries
        for j in range(16):
            p += '%02x' % sbox[i*15 + j] + '  '
        p += '\n'

    return p.upper()
