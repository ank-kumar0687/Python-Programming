import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    email TEXT,
    mobile TEXT,
    city TEXT
)
""")


rollno = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
gender = input("Enter Gender: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
mobile = input("Enter Mobile: ")
city = input("Enter City: ")

try:
    cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (rollno, name, gender, age, email, mobile, city))
    conn.commit()
    print("\nRecord inserted successfully!")
except sqlite3.IntegrityError:
    print("\nError: Roll Number already exists!")


conn.close()
