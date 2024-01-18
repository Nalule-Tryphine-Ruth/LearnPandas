# import libraries
import pandas as pd

# Pandas has 2 main data structures (series and dataframes)

# pandas Series* one-dimensional labeled array
ser = pd.Series(data=[100, 200, 300, 400, 500], index=['tom', 'bob', 'nancy', 'dan', 'eric'])

# pandas Dataframes is a two dimension labelled array

d = {'one' : pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two' : pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}
