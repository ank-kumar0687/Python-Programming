import pandas as pd
import re


df = pd.read_excel("data.xlsx")


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


valid_emails = df[df['Email'].apply(lambda x: bool(re.match(pattern, str(x))))]


print("Students with Valid Emails:")
print(valid_emails)
