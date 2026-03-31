import pandas as pd
import re


df = pd.read_excel("data.xlsx")


pattern = r'^\d{2}-\d{10}$'


valid_mobile = df[df['Phone'].apply(lambda x: bool(re.match(pattern, str(x))))]

print("Students with Valid Mobile Numbers (with country code):")
print(valid_mobile)
