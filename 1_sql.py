
import sqlite3
import os
from turtle import update


def create_database():

    if os.path.exists("mydatabase.db"):
        os.remove("mydatabase.db")

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    return conn,cursor


def create_tables(cursor):

    cursor.execute('''
        CREATE TABLE Students(
            id INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            age INTEGER,
            email VARCHAR UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE Teachers(
            id INTEGER PRIMARY KEY,
            teacher_name VARCHAR NOT NULL,
            teacher_age INTEGER,
            teacher_email VARCHAR UNIQUE
        )
    ''')


def insert_data(cursor):

    # instead of:
    # cursor.execute("INSERT INTO students (name, age, email) VALUES ('ahmet', 30, 'ahmet@hotmail.com')")

    students = [
        (1, 'ahmet', 20, 'ahmet@hotmail.com'),
        (2, 'bugra', 22, 'bugra@hotmail.com'),
        (3, 'ceren', 21, 'ceren@hotmail.com'),
        (4, 'deniz', 19, 'deniz@hotmail.com'),
        (5, 'emre', 20, 'emre@hotmail.com'),
    ]

    teachers = [
        (1, 'halis', 40, 'halis@hotmail.com'),
        (2, 'eda', 32, 'eda@hotmail.com'),
        (3, 'filiz', 51, 'filiz@hotmail.com'),
        (4, 'yesin', 25, 'yesin@hotmail.com'),
    ]


    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?)", students)
    cursor.executemany("INSERT INTO Teachers VALUES (?,?,?,?)", teachers)

    print("sample data inserted okay.")


def basic_sql_operations(cursor):

    # SELECT ALL
    cursor.execute("SELECT * FROM teachers")
    # data = cursor.fetchall()
    # for row in data:
    #     print(row)

    # SELECT SPESIFIC
    cursor.execute("SELECT * FROM teachers WHERE teacher_name='eda'")

    # SELECT BY ORDER
    cursor.execute("SELECT * FROM students ORDER BY AGE")

    # SELECT BY QUANTITY
    cursor.execute("SELECT * FROM students LIMIT 3") # ilk 3 kaydı getirir


def update_delete_operations(conn, cursor):
    # INSERT
    # her columnu verirsen (name, ..) yazmana gerek kalmaz
    # cursor.execute("INSERT INTO students (id, name, age, email) VALUES (6, 'zoe', 26, 'zoe@hotmail.com')")
    cursor.execute("INSERT INTO students VALUES (6, 'zoe', 26, 'zoe@hotmail.com')") # ekledik
    conn.commit()

    # UPDATE
    cursor.execute("UPDATE students SET name='zoé' WHERE name='zoe'")
    conn.commit()

    # DELETE
    cursor.execute("DELETE FROM students WHERE id=6")
    conn.commit()

def aggregate_functions(cursor):
    # COUNT row quantity
    cursor.execute("SELECT COUNT(*) FROM students")

    # AVERAGE
    cursor.execute("SELECT AVG(age) FROM students")

    # MAX-MIN
    cursor.execute("SELECT MAX(age) FROM students")
    cursor.execute("SELECT MIN(age) FROM students")

    # GROUP BY
    cursor.execute("SELECT COUNT(*) FROM students GROUP BY age")

def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''

def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_data(cursor)
        basic_sql_operations(cursor)
        update_delete_operations(conn, cursor)
        aggregate_functions(cursor)
        conn.commit() # cursorin yaptigi isleri apply et

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__=="__main__":
    main()
