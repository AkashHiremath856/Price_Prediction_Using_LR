def get_score():
    from random import randint
    from predict import predict
    import time

    def score():
        f = open('scripts/Datasets/ds_without_dummies.csv', 'r')
        c = f.readlines()

        fm = [line.split(',') for line in c]

        index = randint(1, len(fm))
        actual_val = float(fm[index][3])
        loc = fm[index][0]
        sqft = float(fm[index][1])
        bath = float(fm[index][2])
        bhk = float(fm[index][4])

        pred_price = predict(loc, sqft, bath, bhk)

        if actual_val > pred_price:
            obt = actual_val-pred_price
        else:
            obt = pred_price-actual_val
        if obt < 100:
            return round(100-obt, 3)
        return round(obt-100, 3)

    scores_ = []
    for i in range(20):
        scores_.append(score())

    score_g = (sum(scores_)/len(scores_))

    labels = 'Model Score from 20 Random Datas'
    log_time = '{} '.format(time.ctime())
    score_ = ' {} \n'.format(round(score_g, 3))

    with open('logs/score.txt', 'a') as f:
        f.write(log_time)
        f.write(labels)
        f.write(score_)


get_score()
