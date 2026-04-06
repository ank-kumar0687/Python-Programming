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


cursor.execute("SELECT COUNT(*) FROM student")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO student VALUES (1, 'Ankit', 'Male', 21, 'ankit@gmail.com', '9876543210', 'Rajkot')")
    cursor.execute("INSERT INTO student VALUES (2, 'Riya', 'Female', 20, 'riya@gmail.com', '9123456780', 'Ahmedabad')")
    cursor.execute("INSERT INTO student VALUES (3, 'Rahul', 'Male', 22, 'rahul@gmail.com', '9988776655', 'Surat')")
    conn.commit()


cursor.execute("SELECT * FROM student")

print("Student Records:\n")

row = cursor.fetchone() 

while row is not None:
    print("Roll No:", row[0])
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Email:", row[4])
    print("Mobile:", row[5])
    print("City:", row[6])
    print("------------------------")
    
    row = cursor.fetchone() 


conn.close()
