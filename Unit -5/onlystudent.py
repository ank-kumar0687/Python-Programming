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


roll = int(input("Enter Roll Number to search: "))


cursor.execute("SELECT * FROM student WHERE rollno = ?", (roll,))
row = cursor.fetchone()


if row:
    print("\nStudent Found:\n")
    print("Roll No:", row[0])
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Email:", row[4])
    print("Mobile:", row[5])
    print("City:", row[6])
else:
    print("\nStudent not found!")


conn.close()
