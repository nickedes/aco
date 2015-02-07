from phase1 import *
from phase2 import *
from functions import pretty

s = generate_sbox()

print(pretty(s))

create_matrix(s)