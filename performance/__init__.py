from .nonlinearity1 import nonlinearity
from .bijective import is_bijective
from scipy.linalg import hadamard

def walsh_spectrum(f):
    x = f*hadamard(256)
    length = len(x)
    walsh = []
    for i in range(1,length):
        length_of_list=len(x[i])
        sum = 0
        for j in range(length_of_list):
            sum = sum + x[i][j]
        walsh.append(sum)
    return walsh


def bf_nonlinearity(f, n):
    """ Intermediate non linearity """
    #fw = fwt(f)
    fw = walsh_spectrum(f)
    for i in range(len(fw)):
        fw[i] = abs(fw[i])
    # nonlinearity from the Walsh transform
    return ((2 ** (n - 1)) - (max(fw) / 2))


def bitlist(val):
    """returns a list of the bits after conversion into binary."""
    bitlst = [int(bit) for bit in bin(val)[2:]]
    leng = 8
    while len(bitlst) < leng:
        bitlst.insert(0, 0)
    return bitlst

def test_nonlinearity(sbox):
    """ Test Code for finding nonlinearity"""
    j = 0
    k = 0
    truth_table = [ [ 0 for i in range(8) ] for j in range(256) ]
    for i in range(256):
        truth_table[i] = bitlist(sbox[k*15 + j])
        if j == 15:
            j = 0
            k = k + 1
        else:    
            j = j + 1
    nl = []
    for j in range(8):
        f=[]
        for i in range(256):
            f.append(truth_table[i][j]) 
        nl.append(bf_nonlinearity(f,8))
    return nl                      
    
