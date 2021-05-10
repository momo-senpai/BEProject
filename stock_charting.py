import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import mplfinance as mpf
import datetime as dt
import pandas as pd 
import yfinance as yf

start = dt.datetime(2021,1,15)
end = dt.datetime(2021,3,15)

def data_extraction(Tick, inter):
	# extracting data from Yahoo API
	data = yf.download(tickers=Tick, period ='5d', interval = inter)
	df=pd.DataFrame(data)
	print(data.tail())
	chart(df)
	

def chart(df):
	#charting the stock data
	mpf.plot(df, type='candle', style ='charles', volume=True)
	mpf.show(block=False)

        
def company_data(symbol):
	# getting company data from ticker
	tick = yf.Ticker(symbol)
	company_name = tick.info['longName']
	year_high = tick.info['fiftyTwoWeekHigh']
	year_low = tick.info['fiftyTwoWeekLow']
	day_high = tick.info['dayHigh']
	day_low = tick.info['dayLow']
	mkcap = tick.info['marketCap']
	print(symbol + " : " + company_name)
	print(f"Market Cap : {mkcap}")
	print(f"52 Week High: {year_high}  52 Week Low : {year_low}")
	print(f"Day High: {day_high}  Day Low : {day_low}")



def main():
	Tick = input("Enter Ticker: ")
	inter = input("Enter TimeFrame -> [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo] : ")
	company_data(Tick)
	data_extraction(Tick, inter)


if __name__ == "__main__":
	main()
