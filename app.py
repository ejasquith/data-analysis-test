import pandas as pd 
import pandas_profiling as pp
import numpy as np 

data_frame = pd.read_csv("data/diabetes.csv")
print(data_frame.head())