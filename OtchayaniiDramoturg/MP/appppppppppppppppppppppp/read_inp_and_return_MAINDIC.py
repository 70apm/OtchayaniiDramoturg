from read_const import CountGroup_D, dic_const_z1, dic_const_z2


file_inp = iter([line.rstrip() for line in open('data/abaqus_INP')])        # чтение INP
obl2 = iter([line.rstrip() for line in open('data/2.txt')])                 # чтение эл. входящих во вторую обл.

i = 0

inp_node = {}                   # словарь, содержащий номер узла и его координат
inp_node_list_key = []          # список, состоящий из номеров узлов
inp_node_list_value = []        # список, состоящий из координат узлов

inp_elemets = {}                # словарь, содержащий номер элемента(key) и список узлов, из которых сост. эл(value)
inp_el_list_key = []            # список, состоящий из номеров элементов
inp_el_list_value = []          # список, состоящий из значений каждого элемента (номера узлов из кот. сост. эл.)

data_obl2 = []                  # список, состоящий из номеров элементов 2 области
all_el_and_const_group = {}     # словарь, содержащий номер энергитической группы, элемент и его коэффициенты

for line in file_inp:                                                   # чтение файла
    if line == "*NODE":                                                 # внутреннии границы читаемого файла (начало)
        for line_node in file_inp:                                      # чтение требуемой области
            if line_node == "******* E L E M E N T S *************":    # начало чтения узлов
                break

            line_node = ''.join(line_node.split(','))                   # убираем не нужные знаки
            line_node = line_node.split(" ")

            inp_node_list_key.append(line_node[0])                      # добавляем в список номера узлов
            inp_node_list_value.append(line_node[1:])                   # добавляем в список знач. узлов

    if line == "*ELEMENT, type=T3D2, ELSET=Line1":                      # внутреннии границы читаемого файла (начало)
        for line_elements in file_inp:                                  # чтение требуемой области

            if line_elements == "*ELEMENT, type=CPS3, ELSET=Surface3":  # пропус не требуемой строки
                continue
            if line_elements == "":                                     # конец цикла
                break

            line_elements = ''.join(line_elements.split(','))           # убираем не нужные знаки
            line_elements = line_elements.split(" ")

            inp_el_list_key.append(line_elements[0])                    # добавляем номер элемента в список
            inp_el_list_value.append(line_elements[1:])                 # добавляем значение эл.

for i in range(len(inp_el_list_key)):                                   # построение словаря по элементам
    inp_elemets[inp_el_list_key[i]] = inp_el_list_value[i]

i = 0
for i in range(len(inp_node_list_key)):                                 # построение словаря по узлам
    inp_node[inp_node_list_key[i]] = inp_node_list_value[i]

len_inp_node = len(inp_node)                                            # длинна словаря по узлам

for traxa in obl2:                                                      # чтение файла с эл., кот. входят во 2 обл.

    data_obl2.append(traxa)                                             # добавления в спис. эл. из 2 обл.

for p in range(CountGroup_D):                                           # цикл по энер. группам. p - счётчик

    el_const_all_group = {}                                             # внутр. словарь (эл + конст)

    for data in inp_el_list_key:                                        # чтение списка со значением эл.

        if len(data) !=3:                                               # игнорим одномерные фигуры (линия)

            continue

        else:

            for pp in data_obl2:                                        # чтение эл во второй обл.

                if int(data) == int(pp):                                # проверка каждого эл. на нахож. его во 2 обл.

                    ez = inp_elemets.setdefault(pp)
                    el_const_all_group[tuple(ez)] = dic_const_z2.setdefault(p)  # формирования внутр. словаря
                    break

                else:

                    ez = inp_elemets.setdefault(data)
                    el_const_all_group[tuple(ez)] = dic_const_z1.setdefault(p)


    all_el_and_const_group[p] = el_const_all_group                      # формирование б. сл. (эн.гр + эл + конст)
    range_el = len(el_const_all_group)


print()

