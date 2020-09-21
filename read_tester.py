import pandas as pd

logfile = '/home/jszheng/Downloads/log_0919.txt'

df = pd.read_csv(
    logfile,
    sep="\s+")
print(df)
print(df.head())