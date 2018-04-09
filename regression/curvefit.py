import numpy as np


#import csv
import numpy as np
from sklearn.svm import SVR
#import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime
from datetime import datetime, timedelta


#dates = []
#prices = []

def predict_price(dates, prices, x):
	dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

	svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	svr_lin = SVR(kernel= 'linear', C= 1e3)
	svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
	svr_rbf.fit(dates, prices) # fitting the data points in the models
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)

	plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	#plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	#plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	plt.xlabel('Date')
	plt.ylabel('Price')
	#plt.title('Support Vector Regression')
	#plt.legend()
	plt.show()
	#print svr_rbf.predict(x)
	#print svr_lin.predict(x)
	#print svr_poly.predict(x)
	for i in x:
		print(svr_rbf.predict(dates)[i])
	return svr_rbf.predict(dates)[x], svr_lin.predict(dates)[x], svr_poly.predict(dates)[x]


def get_mdata(symbol):
	all_closes = []
	#start = datetime(2018, 2, 1)
	#end = datetime(2018, 2, 27)
	#today = str(datetime.today().date())
	yday = str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))

	df = DataReader(symbol, 'morningstar', '2018-04-02', yday)
	#print today 
	#print yday

	#print str(datetime.today().date())
	#print datetime.datetime.now() - datetime.timedelta(days = 1)
		#print df
	adj_close = df['Close']
	all_closes += list(adj_close)
	#prices = all_closes
	#print prices
	return all_closes


#get_data('AVGO.csv') # calling get_data method by passing the csv file to it
#prices = Reverse(get_mdata()) # calling get_data method by passing the csv file to it

#portfolio = ["CVS", "QCOM", "AAPL", "AVGO" ,"AMZN", "GOOG", "FB", "WMT"]
portfolio = ["QCOM"]

for stock in portfolio:
	prices = get_mdata(stock)
	dates = np.arange(len(prices))
	print dates
	print prices
	z = np.polyfit(dates, prices, 4)
	p = np.poly1d(z)
	print p
	#predicted_price = predict_price(dates, prices, len(prices)-1)
	print("##############################")
	print("##############################\n")
	
	#print("Total Predicted Price for {0} is".format(stock))
	#print ("The next stock price Open for ", stock)
	#print ("RBF kernel %.2f" % (predicted_price[0]))
	#print ("Linear kernel %.2f" % (predicted_price[1]))
	#print ("Polynomial kernel %.2f" % (predicted_price[2]))
	print("##############################")
	print("##############################\n")
	


#prices = get_mdata("CVS")
#print  prices.reverse
#print prices


#print "Dates- ", dates
#print "Prices- ", prices

	 




#x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
#y = np.array([231, 221, 225, 226, 221, 217])
#z = np.polyfit(x, y, 3)
#print z
p = np.poly1d(z)
print p(5)