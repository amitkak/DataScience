# Predicting Stock Prices with Deep Learning
This is a very simple project that is used to predict future prices of stocks (NOTE: This uses Python 3.6)

# Requirements
- pandas_datareader
- keras
- sklearn
- h5py (for model saving)

# Usage
1. Download the repository via `git clone https://github.com/noahchalifour/stocks_deep_learning`
2. Change into the directory `cd stocks_deep_learning`
3. Install required packages via `pip install -r requirements.txt`
4. Edit `params.py` to the desired settings
5. Execute `python train.py`
6. Test `python test_history -m <model_name> --start_date=<YYYY-MM-DD> --end_date=<YYYY-MM-DD>` OR `python test_live -m <model_name>`

	e.g
Open Mini Conda Shell
set "KERAS_BACKEND=theano"
set "MKL_THREADING_LAYER=GNU"
Edit `params.py` to the desired symbols
python train.py   (This will train the model)
python test_live.py -m 2018-06-18_0 -c 10  (This will predict it. Make sure you have internet connectivity)
Make sure you enter the ticker name as "QCOM"
Make sure the data reader in train.py and test_live.py is iex. If you change in one then corresponding change is needed in the next one as well.
