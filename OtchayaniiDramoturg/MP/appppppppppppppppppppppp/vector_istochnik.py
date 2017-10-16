from read_inp_and_return_MAINDIC import all_el_and_const_group, len_inp_node, CountGroup_D
from bild_local_matrix import el
import numpy as np


def first(vctr = np.ones((int(len_inp_node), 1))):


    Result = {}

    for i in range(CountGroup_D):
        local_dic = {}
        need_vectr = 0
        Group_vctr = np.zeros((3, 1))

        for p in range(len(el)):

            data = tuple(el[p])

            Group_vctr[0, 0] = vctr[int(data[0])-1, 0]
            Group_vctr[1, 0] = vctr[int(data[0])-1, 0]
            Group_vctr[2, 0] = vctr[int(data[0])-1, 0]

            need_vectr = Group_vctr * float(all_el_and_const_group[i][el[p]][3])
            local_dic[el[p]] = need_vectr
        Result[i] = local_dic

    i = 0
    p = 0

    all_el_and_vctr = {}
    for p in range(len(el)):
        local_sours = np.zeros((3, 1))
        for i in range(CountGroup_D):
            local_sours += Result[i][el[p]]

        all_el_and_vctr[el[p]] = local_sours

    return all_el_and_vctr



def gl_vktr(sup):

    global_Vkt = np.zeros((len_inp_node, 1))
    for p in range(len(el)):
        data = sup[el[p]]
        global_Vkt[int(el[p][0]) - 1, 0] += data[0, 0]
        global_Vkt[int(el[p][1]) - 1, 0] += data[1, 0]
        global_Vkt[int(el[p][2]) - 1, 0] += data[2, 0]


    return global_Vkt








