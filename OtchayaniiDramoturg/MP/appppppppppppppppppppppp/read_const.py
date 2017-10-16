const_file = iter([line.rstrip() for line in open('1.txt')])

list_koef_D = []
E_cfd = []
E_trans = []
vE_f = []
Es_g_1 = []
Es_g_2 = []
Es1_g_1 = []

list_koef_D_2 = []
E_cfd_2 = []
E_trans_2 = []
vE_f_2 = []
Es_g_1_2 = []
Es_g_2_2 = []
Es1_g_1_2 = []

dic_const_z1 = {}
dic_const_z2 = {}

koefxa = {}
eg_1_z1 = {}
eg_1_z2 = {}
ecfd_z1 = {}
ecfd_z2 = {}

for line in const_file:

    if line == '--E-group--1zone':
        for D in const_file:
            i = 0
            if D == '':
                break
            D = D.split(' ')
            list_koef_D.append(D[1])
            E_cfd.append(D[2])
            ecfd_z1[i] = D[2]
            E_trans.append(D[3])
            vE_f.append(D[4])
            Es_g_1.append(D[5])
            eg_1_z1[i] = D[5]
            Es_g_2.append(D[6])
            Es1_g_1.append(D[7])
            i += 1

    if line == '--E-group--2zone':
        i = 0
        for D in const_file:
            if D == '':
                break
            D = D.split(' ')
            list_koef_D_2.append(D[1])
            E_cfd_2.append(D[2])
            ecfd_z2[i] = D[2]
            E_trans_2.append(D[3])
            vE_f_2.append(D[4])
            Es_g_1_2.append(D[5])
            eg_1_z2[i] = D[5]
            Es_g_2_2.append(D[6])
            Es1_g_1_2.append(D[7])
            i += 1

    if line == 'koefx':
        i = 0
        for D in const_file:
            if D == '':
                break
            D = D.split(' ')
            koefxa[i] = D[2]
            i += 1


CountGroup_D = len(list_koef_D)

brawl = 0
for brawl in range(CountGroup_D):
    dic_const_z1[brawl] = [list_koef_D[brawl], E_cfd[brawl], E_trans[brawl], vE_f[brawl], Es_g_1[brawl], Es_g_2[brawl], Es1_g_1[brawl]]
    dic_const_z2[brawl] = [list_koef_D_2[brawl], E_cfd_2[brawl], E_trans_2[brawl], vE_f_2[brawl], Es_g_1_2[brawl], Es_g_2_2[brawl], Es1_g_1_2[brawl]]



print()



