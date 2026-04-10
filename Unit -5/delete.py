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

# Take roll number to delete
roll = int(input("Enter Roll Number to delete: "))

# Check if student exists
cursor.execute("SELECT * FROM student WHERE rollno = ?", (roll,))
row = cursor.fetchone()

if row:
    # Delete query
    cursor.execute("DELETE FROM student WHERE rollno = ?", (roll,))
    conn.commit()
    print("\nRecord deleted successfully!")
else:
    print("\nStudent not found!")

# Close connection
conn.close()
