import pandas as pd


df = pd.read_excel("data.xlsx")

print("Original Data:")
print(df)


print("\nAfter using dropna():")
df_drop = df.dropna()
print(df_drop)


print("\nAfter using fillna():")


df_fill = df.fillna({
    'Age': 0,
    'City': 'Unknown',
    'Marks': 0
})

print(df_fill)
