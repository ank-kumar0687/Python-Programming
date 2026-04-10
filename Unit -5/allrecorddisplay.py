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


cursor.execute("""
SELECT * FROM student
WHERE name LIKE 'N____'   -- N + 4 characters = 5 length
""")

rows = cursor.fetchall()


if rows:
    print("\nStudents whose name starts with 'N' and length is 5:\n")
    for row in rows:
        print("Roll No:", row[0])
        print("Name:", row[1])
        print("Gender:", row[2])
        print("Age:", row[3])
        print("Email:", row[4])
        print("Mobile:", row[5])
        print("City:", row[6])
        print("------------------------")
else:
    print("\nNo matching records found!")


conn.close()
