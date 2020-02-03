import pybithumb

all = pybithumb.get_current_price("ALL")
for ticker, data in all.items():
    print(ticker, data['closing_price'])
