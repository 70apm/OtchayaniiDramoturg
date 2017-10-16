from inp_main import (inp_node, inp_el_list_value)
from Global_matrix import m_global
import numpy as np

long = len(inp_node) - 1
a = 0
vector_nag = np.zeros((long, 1))

"формирование граничных условий"

uz = []
asd = []
gr_uslov = np.zeros((long, 1))

ary = 0

for victor in inp_el_list_value:
    if len(victor) == 2:
        for janna in victor:
            uz.append(janna)

for esh in uz:
    if esh not in asd:
        asd.append(esh)

for ary in range(len(asd)):
    gr_uslov[int(asd[ary]) - 1, 0] = asd[ary]

"**********************************"

for mippo in range(long):
    vector_nag[mippo, 0] = 1

matrix = np.zeros((long, long))

i = 0

for i in range(long):  # этап 1: Граничные условия

    if int(gr_uslov[i, 0]) == 0:
        p = 0
        for p in range(long):
            matrix[i, p] = m_global[i + 1, p + 1]

    else:

        matrix[i, i] = m_global[i + 1, i + 1]
        vector_nag[i, 0] = float(gr_uslov[i, 0]) * float(matrix[i, i])

i = 0
j = 0
for i in range(long):  # Этап 2: граничные условия

    if int(gr_uslov[i, 0]) != 0:
        for j in range(long):
            if i == j:
                continue

            else:

                vector_nag[j, 0] = float(vector_nag[j, 0]) - (float(matrix[j, i]) * float(gr_uslov[i, 0]))
                matrix[j, i] = 0

print()
