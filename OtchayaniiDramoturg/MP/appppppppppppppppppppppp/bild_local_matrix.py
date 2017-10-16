from read_inp_and_return_MAINDIC import inp_elemets, inp_node, all_el_and_const_group
import numpy as np

B = np.zeros((2, 3))                            # нулевая матрица для построение локальной матрицы
D_matrix = np.zeros((2, 2))                     # нулевая матрица для коеф. диффузии (D)
el = []                                         # список, созданный для помощи в храении возвращаемых параметров

all_matrix_end_el_group = {}                    # словарь (эн.гр. + эл. + матрица)
Range = len(all_el_and_const_group)             # количество групп

for line_e in inp_elemets:                      # формирование списка элементов
    ZE = inp_elemets.setdefault(line_e)         # получение узлов каждого элемента
    if len(ZE) == 3:                            # условия фильтрации (опускаем одномерные)
        el.append(tuple(ZE))                    # оставшиеся добавляем в список



for i in range(Range):                                          # начало цикла по эн.гр
    matrix_l = []                                               # список матриц для элементов
    pew = 0                                                     # счётчик элемента
    for line in el:                                             # парсинг списка элемента
        matrix_dic = {}                                         # локальная матрица для храниения списка матриц по эн.гр
        morgana = 0                                             # счётчик для чтения узлов каждого элемента
        for morgana in range(3):                                # чтение словаря узлов и нахождения его координат
            data = inp_node.setdefault(line[morgana])
            if morgana == 0:
                Xi = float(data[0])
                Yi = float(data[1])
            if morgana == 1:
                Xj = float(data[0])
                Yj = float(data[1])
            if morgana == 2:
                Xk = float(data[0])
                Yk = float(data[1])
        "Y(b)"
        B[0, 0] = Yj - Yk                                        # формирование матрицы локальной
        B[0, 1] = Yk - Yi
        B[0, 2] = Yi - Yj
        "X(c)"
        B[1, 0] = Xk - Xj
        B[1, 1] = Xi - Xk
        B[1, 2] = Xj - Xi
        A = 1 / 2 * ((Xi - Xk) * (Yj - Yk) - (Xj - Xk) * (Yi - Yk))
        B = (1 / (2 * A)) * B
        B_trans = B.transpose()
        D_matrix[0, 0] = D_matrix[1, 1] = all_el_and_const_group[i][el[pew]][0]

        DB = np.dot(D_matrix, B)
        B_trans_DB = np.dot(B_trans, DB)
        matrix_l.append(B_trans_DB)                             # добавление полученых матриц в список
        pew += 1
    p = 0
    for p in range(len(el)):                                    # формирование внутр. словаря (эл. + матрица)
        matrix_dic[el[p]] = matrix_l[p]

    all_matrix_end_el_group[i] = matrix_dic                     # формирование гл. словоря (эн. гр + эл. + матрица)

print()
