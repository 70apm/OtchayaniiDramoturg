from bild_local_vektor import all_vt_and_const_group
from bild_local_matrix import el
from read_inp_and_return_MAINDIC import len_inp_node
from read_const import CountGroup_D
import numpy as np


all_global_vt_and_group ={}                                 # главный словарь (эн.гр. + глобальный вектор)
Global_vektor = np.zeros((len_inp_node, 1))                 # пустой глобальный вектор
len_global_vector = len(Global_vektor)                      # длинна вектора

for i in range(CountGroup_D):                               # начало цикла по энергии

    Global_vektor = np.zeros((len_inp_node, 1))             # пустой глобальный вектор

    for p in range(len(el)):                                # чтение списка элементов (см. from\import)
        data = all_vt_and_const_group[i][el[p]]             # чтение словаря (эн.гр. + элемент + вектор)

        Global_vektor[int(el[p][0]) - 1, 0] += data[0, 0]   # заполнение глобального вектора
        Global_vektor[int(el[p][1]) - 1, 0] += data[1, 0]
        Global_vektor[int(el[p][2]) - 1, 0] += data[2, 0]

        all_global_vt_and_group[i] = Global_vektor          # гл. матрица (эн. группа + глобальная матрица)


print()