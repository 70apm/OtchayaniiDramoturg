from bild_local_matrix import A, Range
from read_inp_and_return_MAINDIC import (inp_node, inp_el_list_value, all_el_and_const_group)
import math as m
import numpy as np

N_values = []                                                   # список N векторов

all_vt_and_const_group = {}                                     # конечный словарь ( эн.гр. + элем. + вектор )

for pow in range(Range):                                        # цикл, формирование словаря. В данном месте по энергии
    Dic_el_n = {}                                               # локальный словарь ( элем. + вектор)
    k = 0                                                       # счётчик, для формирования словоря
    for line in inp_el_list_value:                              # начало парсинга списка элементов

        if len(line) == 2:                                      # условие фильтрования, отбрасывается одномерные эл.
            continue
        else:
            N_vektor = np.zeros((3, 1))                         # нулевой вектор, для дальнейшего заполнение
            i = 0
            for i in range(3):                                  # в данном цикле, мы рассматриваем каждый уз. элемента
                data = inp_node.setdefault(line[i])             # и достаём координаты каждого узла
                if i == 0:
                    Xi = float(data[0])
                    Yi = float(data[1])
                if i == 1:
                    Xj = float(data[0])
                    Yj = float(data[1])
                if i == 2:
                    Xk = float(data[0])
                    Yk = float(data[1])
            a = m.sqrt(m.pow((Yj - Yi), 2) + m.pow((Xj - Xk), 2))   # математические выкладки по нахождению вектора
            b = m.sqrt(m.pow((Yk - Yj), 2) + m.pow((Xk - Xj), 2))
            c = m.sqrt(m.pow((Yi - Yk), 2) + m.pow((Xi - Xk), 2))
            X_c = (a * Xi + b * Xj + c * Xk) / (a + b + c)
            Y_c = (a * Yi + b * Yj + c * Yk) / (a + b + c)
            "для Ni"
            ai = (Xj * Yk) - (Xk * Yj)
            bi = (Yj - Yk)
            ci = (Xk - Xj)
            Ni = (1 / (2 * A)) * (ai + bi * X_c + ci * Y_c)
            "для Nj"
            aj = (Xk * Yi) - (Yk * Xi)
            bj = (Yk - Yi)
            cj = (Xi - Xk)
            Nj = (1 / (2 * A)) * (aj + bj * X_c + cj * Y_c)
            "для Nk"
            ak = (Xi * Yj) - (Yi * Xj)
            bk = (Yi - Yj)
            ck = (Xj - Xi)
            Nk = (1 / (2 * A)) * (ak + bk * X_c + ck * Y_c)
            N_vektor[0, 0] = Ni
            N_vektor[1, 0] = Nj
            N_vektor[2, 0] = Nk
            N_real = (float(all_el_and_const_group[pow][tuple(line)][4]) + float(all_el_and_const_group[pow][tuple(line)][5]) - float(all_el_and_const_group[pow][tuple(line)][1])) * N_vektor
            N_values.append(N_real)

        Dic_el_n[tuple(line)] = N_real      # формирование внутр словаря (эл. + вектор)
        k += 1

        all_vt_and_const_group[pow] = Dic_el_n   # гл. словарь (груп. энерг. + эл. + вектор)

print()