import pandas as pd 
import csv 

df=pd.read_csv("final.csv")
del df["hyperlink"]
print(df.shape)
