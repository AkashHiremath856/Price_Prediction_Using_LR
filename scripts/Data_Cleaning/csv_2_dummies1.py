def dummies_1():
    f = open('Datasets/ds_without_dummies.csv', 'r')
    c = f.readlines()
    l = []

    for i in range(0, len(c)):
        c[i] = c[i].strip('\n')
        l.append(c[i])

    f = []
    for i in range(len(l)):
        for d in (l[i].split(',')):
            f.append(d)

    def head():
        cl = str(c[0]).split(',')
        for h in cl:
            clc = '{},'.format(h)
            file = open("test.csv", "a")
            file.write(str(clc).strip('\n'))
            file.close

    head()

    def get_location():
        for i in range(0, len(c)):
            c[i] = c[i].strip('\n')
            l.append(c[i])

        f = []
        for i in range(len(l)):
            for d in (l[i].split(',')):
                f.append(d)

        locations = []
        i = 0
        j = 0
        for k in range(len(f)):
            j = i+5  # 0,5,10,15
            try:
                f[j]
            except IndexError:
                break
            locations.append(f[i])
            i = j

        locations_set = set(locations)
        locations_set_sorted = sorted(locations_set)
        locations_set_sorted = locations_set_sorted[:-2]

        for loc in locations_set_sorted:
            tow = '{},'.format(loc)
            file = open("test.csv", "a")
            file.write(str(tow))
            file.close

    get_location()

    # -------------------------------------Head Done--------------------------------------

    def to_csv():
        l = []
        for i in range(1, len(c)):
            c[i] = c[i].strip('\n')
            l.append(c[i])

        f = []
        for i in range(len(l)):
            for d in (l[i].split(',')):
                f.append(d)

        l = ('0,'*240)
        for i in range(0, len(f), 5):
            try:
                f[i+5]
            except IndexError:
                break

            file = open("Datasets/test.csv", "a")
            inp = '\n{},{},{},{},{},{}'.format(str(f[i]), str(
                f[i+1]), str(f[i+2]), str(f[i+3]), str(f[i+4]), l[:])
            file.write(inp)
            file.close

    to_csv()
