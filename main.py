import pandas as pd
import os
import glob

folder = os.getcwd()
files = glob.glob(folder + "/*.csv")

data = []

for file in files:
    df = pd.read_csv(file, index_col=None, header=0)
    data.append(df)

result = pd.concat(data, axis=0, ignore_index=True)
result.to_csv("results/output.csv", index=False)

result["date"] = pd.to_datetime(result["date"])

by_product = pd.pivot_table(result, index=["item", "size"], values=["qty"], aggfunc=sum)
by_country = pd.pivot_table(result, index=["country"], values=["qty"], aggfunc=sum)

by_product.to_csv("results/byproduct.csv")
by_country.to_csv("results/bycountry.csv")
