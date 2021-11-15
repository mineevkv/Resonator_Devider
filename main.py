# Press the green button in the gutter to run the script.


f = open('Nb_cold-all-out.dat', 'r')
line_list = f.readlines()

f_dln = open('Nb_cold-dlin.dat', 'w')
f_dln.write(line_list[0])  # write tittle

f_kor = open('Nb_cold-kor.dat', 'w')
f_kor.write(line_list[0])  # write tittle

f_logfile = open('logfile.txt', 'w')
f_logfile.write('kor' + '\t' + 'dlin' + '\n')  # write tittle



def kor(string):
    """
    write short resonator data
    """

    print(string)
    f_logfile.write(string + '\n')

    string = string.split('-')
    print(int(string[0]), '-',  int(string[1]))
    for line in line_list[int(string[0]) + 2: int(string[1]) + 2]: #  line[0] - tittle //Fbwo
        if float(line.split('\t')[1]) > 1:  # AVER.HW > 1
            f_kor.write(line)
        else:
            print(line.split('\t')[8] + ' - kor_WARNING: AVER.HW < 1')
            f_logfile.write(line.split('\t')[8] + ' - kor_WARNING: AVER.HW < 1' + '\n')
    return


def dln(string):
    """
    write long resonator data
    """
    print('\t\t\t' + string)
    f_logfile.write('\t' + string + '\n')

    string = string.split('-')
    for line in line_list[int(string[0]) + 1: int(string[1]) + 1]:
        if float(line.split('\t')[1]) > 1:  # AVER.HW > 1
            f_dln.write(line)
        else:
            print(line.split('\t')[8] + ' - dln_WARNING: AVER.HW < 1')
            f_logfile.write(line.split('\t')[8] + ' - dln_WARNING: AVER.HW < 1' + '\n')
    return 0


if __name__ == '__main__':

    dln('0-28')

    kor('29-87')
    kor('88-148')
    kor('149-220')
    kor('221-254')

    dln('255-283')

    kor('284-317')
    kor('318-351')
    kor('352-385')

    dln('386-414')

    kor('415-448')
    kor('449-482')
    kor('483-516')

    dln('517-545')

    kor('546-579')
    kor('580-613')

    dln('614-642')

    kor('643-676')
    kor('677-710')

    dln('711-739')

    kor('740-772')

    dln('773-801')

    kor('802-834')

    dln('835-863')

    kor('864-896')

    dln('897-925')
    dln('926-954')

    kor('955-988')

    dln('989-1016')

    kor('1017-1050')

    dln('1051-1078')

    kor('1079-1112')

    dln('1113-1140')

    kor('1141-1174')

    dln('1175-1202')

    kor('1203-1236')

    kor('1237-1270')

    dln('1271-1299')

    kor('1300-1332')

    dln('1333-1361')

    kor('1362-1393')

    dln('1394-1422')

    kor('1423-1455')

    dln('1456-1484')

    kor('1485-1517')

    dln('1518-1546')

    kor('1547-1579')

    dln('1580-1607')

    kor('1608-1640')

    dln('1641-1666')

    kor('1667-1700')

    dln('1701-1728')  # 1729???

    # hardcode: '1730-1762' = 1730 -1 - 1762 - 1'
    kor('1730-1762') # 1763 warning

    dln('1763-1791')

    f.close()
    f_dln.close()
    f_kor.close()


    f_dln = open('Nb_cold-dlin.dat', 'r')
    line_data_dln = f_dln.readlines()
    hw_dln = 0
    for line_dln in line_data_dln[1:]:
        hw_dln = max(hw_dln, float(line_dln.split('\t')[1]))

    f_kor = open('Nb_cold-kor.dat', 'r')
    line_data_kor = f_kor.readlines()
    hw_kor = 1000
    for line_kor in line_data_kor[1:]:
        hw_kor = min(hw_kor, float(line_kor.split('\t')[1]))

    print('HW_dln_MAX = ', hw_dln, '\t', 'HW_kor_MIN = ', hw_kor)
    f_logfile.write('HW_dln_MAX = ' + str(hw_dln) + '\n' + 'HW_kor_MIN = ' + str(hw_kor))

    for line_kor in line_data_kor[1:]:
        if float(line_kor.split('\t')[1]) < hw_dln:
            print(line_kor.split('\t')[8], ' - kor_WARNING: HW_kor < HW_dln_MAX')
            f_logfile.write(line_kor.split('\t')[8] + ' - kor_WARNING: HW_kor < HW_dln_MAX' + '\n')

    for line_dln in line_data_dln[1:]:
        if float(line_dln.split('\t')[1]) > hw_kor:
            print(line_dln.split('\t')[8], ' - dln_WARNING: HW_dln > HW_kor_MIN')
            f_logfile.write(line_dln.split('\t')[8] + ' - dln_WARNING: HW_dln > HW_kor_MIN' + '\n')



    f_dln.close()
    f_kor.close()
    f_logfile.close()