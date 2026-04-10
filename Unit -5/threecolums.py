import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()


columns = []

n = int(input("Enter number of columns: "))


for i in range(n):
    print(f"\nEnter details for column {i+1}:")
    col_name = input("Column Name: ")
    data_type = input("Data Type (varchar/int): ")
    size = input("Size: ")
    
    
    columns.append((col_name, data_type, size))

print("\nColumn List:")
for col in columns:
    print(col)


table_name = input("\nEnter table name: ")

query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

field_list = []

for col in columns:
    name, dtype, size = col
    
    if dtype.lower() == "varchar":
        field_list.append(f"{name} TEXT")  
    elif dtype.lower() == "int":
        field_list.append(f"{name} INTEGER")
    else:
        field_list.append(f"{name} TEXT")

query += ", ".join(field_list) + ")"


cursor.execute(query)

print(f"\nTable '{table_name}' created successfully!")


conn.close()
