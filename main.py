stocks_dict = {
  "AAPL" : "169.68", 
  "MFST" : "307.26", 
  "GOOGL" : "107.34", 
  "AMZN" : "105.45",
  "TSLA" : "164.31",
  "INTC": "31.06",
  "META": "240.32",
  "NFLX": "329.93",
  "WMT": "150.97",
  "BA": "206.78"
}
tickers = input('Please Enter a ticker symbol (e.g AMZN). Type QUIT to stop: ')
while not tickers == "QUIT":
  if tickers in stocks_dict:
    print('{} : {}' .format(tickers, stocks_dict[tickerss]))
  else:
    print('{} not found' .format(tickers))
  tickers = input('Please enter a ticker symbol (e.g AMZN) Type QUIT to stop: ')