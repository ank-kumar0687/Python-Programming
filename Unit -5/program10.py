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


def insert_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")
    city = input("Enter City: ")

    try:
        cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (roll, name, gender, age, email, mobile, city))
        conn.commit()
        print("Inserted successfully!")
    except:
        print("Error! Roll number may exist.")

def list_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    for r in rows:
        print(r)

def search_student():
    roll = int(input("Enter Roll No: "))
    cursor.execute("SELECT * FROM student WHERE rollno=?", (roll,))
    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Not found!")

def update_student():
    roll = int(input("Enter Roll No: "))
    cursor.execute("SELECT * FROM student WHERE rollno=?", (roll,))
    
    if cursor.fetchone():
        name = input("New Name: ")
        gender = input("New Gender: ")
        age = int(input("New Age: "))
        email = input("New Email: ")
        mobile = input("New Mobile: ")
        city = input("New City: ")

        cursor.execute("""
        UPDATE student SET name=?, gender=?, age=?, email=?, mobile=?, city=?
        WHERE rollno=?""",
        (name, gender, age, email, mobile, city, roll))

        conn.commit()
        print("Updated successfully!")
    else:
        print("Not found!")

def delete_student():
    roll = int(input("Enter Roll No: "))
    cursor.execute("SELECT * FROM student WHERE rollno=?", (roll,))
    
    if cursor.fetchone():
        cursor.execute("DELETE FROM student WHERE rollno=?", (roll,))
        conn.commit()
        print("Deleted successfully!")
    else:
        print("Not found!")

# Menu
while True:
    print("\n1.Insert\n2.Update\n3.Search\n4.Delete\n5.List\n6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_student()
    elif ch == 2:
        update_student()
    elif ch == 3:
        search_student()
    elif ch == 4:
        delete_student()
    elif ch == 5:
        list_students()
    elif ch == 6:
        break
    else:
        print("Invalid choice!")

conn.close()
