from pandas import DataFrame

data = {"open": [730, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]}

df = DataFrame(data, index=["2018-01-01", "2018-01-02"])
print(df.loc["2018-01-01"])
print(df.iloc[1])

target = ["2018-01-01", "2018-01-02"]
print(df.loc[target])

target = [0, 1]
print(df.iloc[target])
