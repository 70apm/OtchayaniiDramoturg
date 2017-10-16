from read_inp_and_return_MAINDIC import (inp_el_list_value, len_inp_node, CountGroup_D)
from bild_local_matrix import all_matrix_end_el_group
import numpy as np




data_el = []                                                        # вспомогательный список элементов
np.set_printoptions(threshold=np.nan)
all_global_matirx_and_group = {}                                    # Главный словарь ( энерг.группа. + глобал матрица)

for pow in range(CountGroup_D):                                     # счётчик по энергии
    k = 0                                                           # счётчик для формирования словаря(all_global_matix_and_group
    m_global = np.zeros((len_inp_node, len_inp_node))               # нулевая внутр. матрица
    for line_el in inp_el_list_value:                               # чтение элементов

        if len(line_el) == 3:                                       # неоюходимое условие, отсев одномерных элементов

            data_el.append(line_el)                                 # добавление в список всех элементов

            data = all_matrix_end_el_group[pow][tuple(line_el)]     # вытаскиваение из словаря необходимые матрицы для каждого элемента

            for p in range(3):                                      # заполнение глобальной матрицы

                for i in range(3):

                    m_global[int(line_el[p]) - 1, int(line_el[i]) - 1] += float(data[p, i])

        k += 1
    all_global_matirx_and_group[pow] = m_global                     # формирование главного словаря (эн.гр. + глобальная матрица)

print()



