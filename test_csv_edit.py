import pandas as pd
df = pd.read_csv("produtoskalli_kalli_teste1.csv")
print(df[1:1])
print(df['P'].replace("\n0" ,"\n"))
