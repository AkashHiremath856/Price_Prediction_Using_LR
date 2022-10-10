from csv_2_dummies1 import dummies_1


def get_dummies():
    dummies_1()
    f = open('Datasets/test.csv', 'r')
    c = f.readlines()

    l = []
    fm = [line.split(',') for line in c]

    rows = 6114

    for j in range(5, len(fm[0])):
        for i in range(1, rows+1):
            if fm[0][j] == fm[i][0]:
                fm[i][j] = 1

    fw = open('Datasets/dummies_done.csv', 'a')
    j = 0
    c = 0
    for i in range(rows):
        j += 1
        for fi in fm[i][1:-1]:
            c += 1
            if c == j*244:
                fiw = '{}'.format(fi)
            else:
                fiw = '{},'.format(fi)
            fw.write(fiw)
        fw.write('\n')
