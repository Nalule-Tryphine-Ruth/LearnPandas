# import libraries
import pandas as pd

# Pandas has 2 main data structures (series and dataframes)

# pandas Series* one-dimensional labeled array
ser = pd.Series(data=[100, 200, 300, 400, 500], index=['tom', 'bob', 'nancy', 'dan', 'eric'])

# pandas Dataframes is a two dimension labelled array

d = {'one' : pd.Series([100., 200., 300.], index=['stars', 'moon', 'pillows']),
     'two' : pd.Series([111., 222., 333., 4444.], index=['stars', 'pillows', 'cerill', 'dancy'])}

df = pd.DataFrame(d)
print(df)

# Create DataFrame from list of Python dictionaries
data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora': 10, 'alice': 20}]


