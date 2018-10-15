import numpy as np
import math
import pandas_datareader.data as web
from datetime import datetime
from datetime import datetime, timedelta

#https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly

def get_mdata(symbol):
	all_closes = []
	today = str(datetime.today().date())
	yday = str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))

	df = web.DataReader(symbol, 'iex', '2018-09-02', yday)
	#print today 
	#print yday

	#print str(datetime.today().date())
	#print datetime.datetime.now() - datetime.timedelta(days = 1)
	#print df
	adj_close = df['close']
	all_closes += list(adj_close)
	prices = all_closes
	#print prices
	return all_closes

portfolio = ["QCOM", "AAPL", "SPY" ,"AMZN", "GOOG", "FB", "GLD"]
#portfolio = ["QCOM"]

for stock in portfolio:
	prices = get_mdata(stock)
	dates = np.arange(1, len(prices)+1)
	#print (dates)
	#print (prices)
	

	x = np.array(dates)
	y = np.array(prices)
	z = np.polyfit(np.log(x), y, 1)
	#print z[0]
	print("##############################")
	print("##############################\n")
	print("Total Predicted Price for {0} is".format(stock))
	
	#print z[1]
	
	 #y = B log(x) + Amplitude
	print ("Amplitude of Move %.2f" % (z[1]))
	print ("B of Move %.2f" % (z[0]))
	print ("Two Days from Today %.2f" % (z[1]+z[0]*math.log(len(prices)+2)))
	print ("Week from Today %.2f" % (z[1]+z[0]*math.log(len(prices)+5)))
	print ("Two Weeks from Today %.2f" % (z[1]+z[0]*math.log(len(prices)+10)))
	
	#print ("Two Days from Today %.2f" % (z[1]+z[0]*math.log(2)))
	#print ("Week from Today %.2f" % (z[1]+z[0]*math.log(5)))
	#print ("Week from Today %.2f" % (z[1]+z[0]*math.log(10)))
	print("##############################")
	print("##############################\n")
