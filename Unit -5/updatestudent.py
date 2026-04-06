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


roll = int(input("Enter Roll Number to update: "))


cursor.execute("SELECT * FROM student WHERE rollno = ?", (roll,))
row = cursor.fetchone()

if row:
    print("\nEnter new details:\n")
    
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")
    city = input("Enter City: ")

    
    cursor.execute("""
    UPDATE student
    SET name = ?, gender = ?, age = ?, email = ?, mobile = ?, city = ?
    WHERE rollno = ?
    """, (name, gender, age, email, mobile, city, roll))

    conn.commit()
    print("\nRecord updated successfully!")
else:
    print("\nStudent not found!")


conn.close()
