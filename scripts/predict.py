from train_model import train

fm, pred, coef, intercept = train()


def predict(loc, sqft, bath, bhk):

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
    return sum+intercept


print(predict('Varthur', 1385.0, 2.0, 2))
