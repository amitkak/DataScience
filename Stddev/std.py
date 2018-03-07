# Enter your code here. Read input from STDIN. Print output to STDOUT
import json
import math
import scipy.stats.stats as st
from datetime import datetime, timedelta
from pandas_datareader import DataReader
import matplotlib.pyplot as plt

#'''
def plotHisto(data):
    """plot the histogram data to visualize"""
    
    plt.hist(data)
    plt.title("Gaussian Histogram")
    plt.xlabel("year")
    plt.ylabel("Frequency")
    plt.show()
#'''


def compute_rmse(arr):
    """computes rmse (root mean square error)"""

    # compute mean
    mean = sum(arr) / len(arr)
    sse = 0

    # loop through the list
    for i in arr:

        # compute sse as (val - mean)^2
        sse += (i - mean) ** 2

    # compute rmse and return
    rmse = math.sqrt(sse) / len(arr)
    return rmse


def compute_stddev(arr):
    """computes standard deviation"""

    # compute mean
    mean = sum(arr) / len(arr)
    sse = 0

    # loop through the list
    for i in arr:

        # compute sse as (val - mean)^2
        sse += (i - mean) ** 2

    # compute std deviation and return
    stddev = math.sqrt(sse / len(arr))
    one_stddev_dn = mean + -1 * stddev
    one_stddev_up = mean + 1 * stddev
    
    return one_stddev_up , one_stddev_dn


def compute_2stddev(arr):
    """compute two standard deviation"""

    # compute mean
    mean = sum(arr) / len(arr)
    sse = 0

    # loop through the list
    for i in arr:

        # compute sse as (val - mean)^2
        sse += (i - mean) ** 2

    # compute two std deviation and return
    stddev = math.sqrt(sse / len(arr))
    two_stddev_dn = mean + -2 * stddev
    two_stddev_up = mean + 2 * stddev
    
    return two_stddev_up , two_stddev_dn


def check_regression(rmse_lst, stddev, skewnessList, skewness_stddev, date_lst):
    """check for regression and if found return the date else return empty string"""

    # initialize max value as lists first value
    maxVal = rmse_lst[0]

    # initialize regression date as empty string.
    # If regression no regression return empty string else return regression
    # date
    reg_date = ""

    # loop through rmse list
    for i in range(0, len(rmse_lst) - 1):

        # calculate absolute difference
        val = abs(rmse_lst[i] - rmse_lst[i + 1])

        # calculate absolute skewness difference
        skewVal = abs(skewnessList[i] - skewnessList[i + 1])

        # conditions check for finding regression
        if (val > stddev) and (i > 1) and (skewVal > skewness_stddev):
            reg_date = date_lst[i + 1]
            return reg_date
    return reg_date


def get_mdata(symbol):
	all_closes = []
	#start = datetime(2018, 2, 1)
	#end = datetime(2018, 2, 27)
	#today = str(datetime.today().date())
	yday = str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))

	df = DataReader(symbol, 'morningstar', '2018-02-02', yday)
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


def main():
    """main function"""

portfolio = ["CVS", "QCOM", "AAPL", "AVGO" ,"AMZN", "GOOG", "FB", "WMT"]

#portfolio = ["QCOM"]

for stock in portfolio:
	prices = get_mdata(stock)
	#dates = np.arange(len(prices))

	histogram = prices
	#rmse = compute_rmse(histogram)
	stddevUp , stddevDn = compute_stddev(histogram)
	stdDev2Up , stdDev2Dn = compute_2stddev(histogram)
	#plotHisto(histogram)
	print stock + "\t" + str(stdDev2Up) + "\t" + str(stddevUp) + "\t" + str(stddevDn) +  "\t"  + str(stdDev2Dn) + "  \n"

if __name__ == "__main__":
    main()