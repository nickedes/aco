from .nonlinearity1 import nonlinearity

def is_bijective(s):
	""" Checks if the s box is bijective """
	for i in range(len(s)):
		if i not in s:
			return False
	return True


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
    
