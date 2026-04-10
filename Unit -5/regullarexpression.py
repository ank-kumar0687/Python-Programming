import pandas as pd
import re


data = {
    'Name': ['Ankit', 'Ravi', 'Priya', 'Simran'],
    'Email': ['ankit123@gmail.com', 'ravi#gmail.com', 'priya@gmail.com', 'simran@.com']
}

df = pd.DataFrame(data)


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


valid_emails_df = df[df['Email'].apply(lambda x: re.match(pattern, x) is not None)]

print("Students with valid email addresses:\n")
print(valid_emails_df)
