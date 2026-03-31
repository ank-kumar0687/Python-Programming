import pandas as pd


df = pd.read_excel(r"D:\4110\unit-4\data.xlsx")


print("Students from Rajkot City:")
print(df[df['City'] == 'Rajkot'])


print("\nMale Students:")
print(df[df['Gender'] == 'Male'])


print("\nMale Students from Rajkot City:")
print(df[(df['City'] == 'Rajkot') & (df['Gender'] == 'Male')])


print("\nStudents with Age >= 20:")
print(df[df['Age'] >= 20])
