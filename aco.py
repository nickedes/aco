from phase1 import *
from phase2 import *
from phase3 import *
from functions import pretty

s = generate_sbox()

print(pretty(s))

mat = create_matrix(s)

x = run_aco(mat)

x[1][255] = 58
print(x[1][255])