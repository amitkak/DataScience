#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:21:50 2017

@author: zaghlol
"""
#import lib and data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

training_set=pd.read_csv('QCOM_Train.csv')
training_set=training_set.iloc[:,1:2].values

#feat scaling
from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
training_set=sc.fit_transform(training_set)
Xtrain=training_set[0:489]
Ytrain=training_set[1:490]

#shaping data
Xtrain=np.reshape(Xtrain,(489,1,1))

#RNN model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

reg=Sequential()

#reg.add(LSTM(units=4,activation='sigmoid',input_shape=(None,1)))
reg.add(LSTM(units=4,activation='relu',input_shape=(None,1)))
#reg.add(LSTM(units=4,activation='softmax',input_shape=(None,1)))

reg.add(Dense(units=1))

#reg.compile(optimizer='adam',loss='mean_squared_error')
#reg.compile(optimizer='adadelta',loss='mean_squared_error')
reg.compile(optimizer='rmsprop',loss='mean_squared_error')

reg.fit(Xtrain,Ytrain,batch_size=32,epochs=200)

test_set=pd.read_csv('QCOM_Test.csv')
real_stock_price=test_set.iloc[:,1:2].values

#getting the prediction 2017
inputs=real_stock_price
inputs=sc.transform(inputs)
inputs=np.reshape(inputs,(35,1,1))

predicted=reg.predict(inputs)

predicted=sc.inverse_transform(predicted)

plt.plot(real_stock_price,color='red',label='Real Stock Price')
plt.plot(predicted,color='blue',label='Predicted Stock Price')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

#getting the real stock price
RST=pd.read_csv('QCOM_Train.csv')
RST=RST.iloc[:,1:2].values
#predicted stock price 
predict_stock_price_train=reg.predict(Xtrain)
predict_stock_price_train=sc.inverse_transform(predict_stock_price_train)

plt.plot(RST,color='red',label='Real Stock Price')
plt.plot(predict_stock_price_train,color='blue',label='Predicted Stock Price')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

#evaluate RNN
import math
from sklearn.metrics import mean_squared_error 
rmse=math.sqrt(mean_squared_error(real_stock_price,predicted))
error=rmse/800 #mean error devided by the avg

