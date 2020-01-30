from pandas import *

data = {"open": [730, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]}

df = DataFrame(data)
upper = df["open"] * 1.3
df["upper"] = upper
print(df)