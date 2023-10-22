import itertools
import re

def f(vars):
    x, y, z, w = vars
    return ((x == (w or y)) or ((w <= z) and (y <= w)))

matrix = ['1..10', '...10', '1.1.0']
num_vars = len(matrix[0]) - 1

table = [''.join(map(str, vars)) + str(int(f(vars))) for vars in itertools.product([0, 1], repeat=num_vars)]

for perm in itertools.permutations(range(num_vars)):
    perm_table = [''.join([line[perm[i]] for i in range(num_vars)]) + line[-1] for line in table]
    for lines in itertools.permutations(perm_table, len(matrix)):
        if re.search(''.join(matrix), ''.join(lines)):
            print(''.join(['xyzw'[perm[i]] for i in range(num_vars)]))
