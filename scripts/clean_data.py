import pandas as pd

df=pd.read_csv("messy_sales_data.csv")

print(df.head())

print(df.info())

df=df.drop_duplicates()

df['Name'].fillna("Unknown", inplace=True)
df["Country"].fillna("India",inplace=True)
df["Plan"].fillna("Basic",inplace=True)

df["Plan"] = df["Plan"].str.capitalize()
df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

print(df.info())

print("Total Sales:",df["Amount"].sum())

print(df.groupby("Country")["Amount"].sum())

print(df.groupby("Plan")["Amount"].sum())

df.to_csv("clean_sales_data.csv", index=False)