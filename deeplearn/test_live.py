from keras.models import model_from_json
import pandas_datareader.data as web
from pandas_datareader._utils import RemoteDataError
from datetime import datetime
import os
import json
import pickle
import argparse
import numpy as np

FILE_DIR = os.path.dirname(os.path.realpath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument('-m', '--model', required=True, type=str)
ap.add_argument('-c', '--checkpoint', required=True, type=str)

args = vars(ap.parse_args())

model_name = args['model']

with open(os.path.join(FILE_DIR, 'models/{}/checkpoints/checkpoint-{}/model.json'.format(model_name, args['checkpoint'])), 'r') as f:
    model = model_from_json(f.read())

model.load_weights(os.path.join(FILE_DIR, 'models/{}/checkpoints/checkpoint-{}/model.h5'.format(model_name, args['checkpoint'])))

with open(os.path.join(FILE_DIR, 'models/{}/scaler.pkl'.format(model_name)), 'rb') as f:
    scaler = pickle.load(f)

with open(os.path.join(FILE_DIR, 'models/{}/params.json'.format(model_name)), 'r') as f:
    params = json.load(f)

print('Loaded model {}.'.format(model_name))

stock_ticker = input("Enter a stock symbol: ")
#stock_ticker = "QCOM"
 
while stock_ticker != "":
    while stock_ticker not in params['symbols']:
        print('Model not trained on', stock_ticker)
        stock_ticker = input("Enter a stock symbol: ")

    now = datetime.now()

    stock_data = None
    i = 0
    while stock_data is None:
        try:
            if i == 5:
                raise Exception('Could not get data for', stock_ticker)
            i += 1
            stock_data = web.DataReader(stock_ticker, 'iex', start=datetime(now.year - 1, now.month, now.day),
                                    end=datetime.today())
            #print stock_data;
        except RemoteDataError:
            continue

    x = np.array(list(stock_data['close'][len(stock_data['close'])-params['chunk']:])).reshape(-1, 1)
    x = scaler.transform(x)

    prediction = model.predict(np.array([x]))

    decoded_prediction = scaler.inverse_transform(prediction)[0][0]

    print('Tomorrow\'s predicted price for {} is {}$.'.format(stock_ticker, round(decoded_prediction, 2)))

    stock_ticker = input("Enter a stock symbol: ")
