def train():
    f = open('bhp.csv', 'r')
    intercept = -20.1324178525028543
    c = f.readlines()

    fm = [line.split(',') for line in c]

    cf = open('logs/coef.txt', 'r')
    coef_ = (cf.readline())
    coef_ = coef_.strip(' ')
    coef_ = coef_.strip('[')
    coef_ = coef_.strip(']')
    coef_ = (coef_).split(',')
    coef_ = [float(c) for c in coef_]

    pred = []
    for i in range(len(coef_)):
        pred.append(0)

    fm[0][-1] = fm[0][-1].strip('\n')
    fm[0].pop(2)
    return fm, pred, coef_, intercept
