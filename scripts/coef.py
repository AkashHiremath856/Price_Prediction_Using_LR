def coef():
    f = open('bhp.csv', 'r')
    c = f.readlines()

    fm = [line.split(',') for line in c]

    # ----------x1-x243,y--------------

    def x_():
        x_ = []

        for i in range(0, 243):
            x = []
            for j in range(1, 6114):
                if i == 2:
                    continue
                x.append(float(fm[j][i]))
            x_.append(x)

        y_ = []
        for i in range(1, len(fm)):
            y_.append(float(fm[i][2]))

        return x_

    # ---------------x1*x1-----------

    def x_pow_2():
        x_pow2 = []

        for i in range(0, 243):
            x = []
            for j in range(1, 6114):
                if i == 2:
                    continue
                x.append(pow(float(fm[j][i]), 2))
            x_pow2.append(x)

        return x_pow2

    # ------------x1*x2*---x243-------------

    def x1_mul_x2_():
        x1_mul_x2 = []

        for i in range(0, 243):
            x = []
            for j in range(1, 6114):
                if i == 2:
                    continue
                x.append(float(fm[j][i])*float(fm[j][i+1]))
            x1_mul_x2.append(x)

        return x1_mul_x2

    # -------------x1*y,x2*y----------------

    def x_mul_y():
        x_mul_y = []

        for i in range(243):
            x = []
            for j in range(1, 6114):
                if i == 2:
                    continue
                x.append(float(fm[j][i])*float(fm[j][2]))
            x_mul_y.append(x)

        return x_mul_y

    # -----------summation_x^2-------------

    def summation_x_pow_2():
        x_pow2 = x_pow_2()
        _x_ = x_()

        summation_x_pow_2 = []

        for i in range(len(_x_)):
            sm = sum(x_pow2[i])
            sub = (sum(_x_[i])*sum(_x_[i]))/6114
            summation_x_pow_2.append(sm-sub)

        return summation_x_pow_2

    # -----------summation_xy-------------

    def summation_x_y():
        summation_x_y = []
        _x_ = x_()

        _x_mul_y = x_mul_y()
        y_ = []
        for i in range(1, len(fm)):
            y_.append(float(fm[i][2]))

        for i in range(len(_x_)):
            sm = sum(_x_mul_y[i])
            sub = (sum(_x_[i])*sum(y_))/6114
            summation_x_y.append(sm-sub)

        return summation_x_y

    # -----------summation_x1x2-------------

    def summation_x_x():
        x1_mul_x2 = x1_mul_x2_()

        summation_x_x = []
        _x_ = x_()

        for i in range(len(x1_mul_x2)):
            sm = sum(x1_mul_x2[i])
            try:
                sub = (sum(_x_[i])*sum(_x_[i+1]))/6114
            except IndexError:
                sub = (sum(_x_[i])*sum(_x_[0]))/6114
            summation_x_x.append(sm-sub)

        return summation_x_x

    # --------------------b1,b2---------------------

    _summation_x_x = summation_x_x()
    _summation_x_pow_2 = summation_x_pow_2()
    _summation_x_y = summation_x_y()

    _coef = []

    for i in range(len(_summation_x_y)):

        div = (_summation_x_pow_2[i]*_summation_x_y[i]) - \
            (sum(_summation_x_x) * _summation_x_y[1])

        quo = (_summation_x_pow_2[i] *
               _summation_x_pow_2[i])-(sum(_summation_x_x)**2)

        res = "{:.8e}".format(div-quo)

        _coef.append(res)

    with open('logs/coef.txt', 'w') as f:
        f.write(str(_coef))

    y_ = []
    for i in range(1, len(fm)):
        y_.append(float(fm[i][2]))

        inter = sum(y_)/len(y_)
