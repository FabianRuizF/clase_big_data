import pandas as pd
import numpy as np

list_of_numbers = np.arange(10000000)

def square(number_argument):
    return number_argument*number_argument

df = pd.DataFrame(list_of_numbers,columns=["number"])

%%timeit -n 3 -r 3
for index,row in df.iterrows():
    row["square"] = row["number"]*row["number"]

df = pd.DataFrame(list_of_numbers,columns=["number"])

%%timeit -n 3 -r 3
df["square"] = df["number"].apply(square)

