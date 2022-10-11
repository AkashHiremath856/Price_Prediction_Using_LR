from pymongo import MongoClient
import time
from predict import predict

print('Server Running')

key = 'helloworld'
timeout = 10000

req = 'mongodb+srv://Akash:{}@cluster0.6pagbip.mongodb.net/?retryWrites=true&w=majority'.format(
    key)

client = MongoClient(req)
db = client.get_database('PredictionData')
recordPrice = db.results

i = 0


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

for i in range(timeout):
    fetchedPrice = list(recordPrice.find())
    pf = fetchedPrice[0]['price']
    l = get()
    x = location
    y = str(l['location'])

    if x != y:
        starttime = time.time()
        location = str(l['location'])
        sqft = l['sqft']
        bath = l['bath']
        bhk = l['bhk']
        print('not same')

        i += 1
        if i == 1:
            continue

        # predict fun
        price_predicted = predict(location, sqft, bath, bhk)
        print(price_predicted)

        # price
        recordPrice.replace_one(
            {'price': pf}, {'price': round(price_predicted, 3)})

    else:
        print('same')
        get()
