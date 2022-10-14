from train_model import train


def predict(loc, sqft, bath, bhk):
    fm, pred, coef, intercept = train()

    location = fm[0].index(loc)
    pred[0] = sqft
    pred[1] = bath
    pred[2] = bhk
    pred[location] = 1

    sum = 0
    l = []
    for i in range(len(pred)):
        l.append(pred[i]*coef[i])
    for lc in range(location):
        sum += l[lc]
    s = 0
    s = sum+intercept
    return round(s, 3)
