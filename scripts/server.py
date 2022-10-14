from pymongo import MongoClient
import time
from predict import predict

print('Server Running')

key = 'helloworld'

req = 'mongodb+srv://Akash:{}@cluster0.6pagbip.mongodb.net/?retryWrites=true&w=majority'.format(
    key)

client = MongoClient(req)
db = client.get_database('PredictionData')
recordPrice = db.results


def get():
    # Mongo DB
    records = db.datas
    fetched = list(records.find())
    l = fetched[-1]
    return l


location = ' '
sqft = ' '
bath = ' '
bhk = ' '

i = 0

for i in range(1000):
    l = get()

    if location != str(l['location']) or bath != l['bath'] or bhk != l['bhk']:
        starttime = time.time()
        location = str(l['location'])
        sqft = l['sqft']
        bath = l['bath']
        bhk = l['bhk']
        # print('not same')

        def write_pr(price_predicted):
            recordPrice.replace_one(
                {'price': pf}, {'price': round(price_predicted, 3)})

            log_time = '{} '.format(time.ctime())
            log_args = '{},{},{},{} '.format(location, sqft, bath, bhk)
            price_val = '{} \n'.format(
                str(round(price_predicted, ndigits=2)))
            labels = '[time, location, sqft, bath, bhk, price]\n'

            with open('logs/logs.txt', 'a') as f:
                f.write(labels)
                f.write(log_time)
                f.write(str(log_args))
                f.write(price_val)

        fetchedPrice = list(recordPrice.find())
        pf = fetchedPrice[0]['price']

        i += 1
        if i == 1:
            continue

        price_predicted = predict(location, sqft, bath, bhk)

        # print('pf', pf)
        # print('price_predicted', price_predicted)

        # price
        if pf != price_predicted:
            write_pr(price_predicted)

        elif pf != price_predicted:
            write_pr(price_predicted)

        else:
            price_predicted = predict(location, sqft, bath, bhk)
            write_pr(price_predicted)

    else:
        # print('same')
        get()
