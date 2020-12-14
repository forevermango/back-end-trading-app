import yfinance

data_frame = yfinance.download('AAPL', start='2020-01-01', end='2020-10-02')
data_frame.to_csv('AAPL.csv')

