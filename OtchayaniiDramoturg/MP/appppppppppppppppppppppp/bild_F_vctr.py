from bild_global_vektor import all_global_vt_and_group
from vector_istochnik import first, gl_vktr
from read_const import koefxa, CountGroup_D


none_vl = gl_vktr(first())
dic_F = {}
Kef = 1

for i in range(CountGroup_D):

    F = ((float(koefxa[i]) * none_vl) / Kef) + all_global_vt_and_group[i]
    dic_F[i] = F






