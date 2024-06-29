import sqlite3

def create_database(db_name):
    """
    Creates a new SQLite database and a students table with columns: id, name, age, and grade.

    Parameters:
    db_name (str): The name of the database to create.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_student(db_name, student_data):
    """
    Inserts a new student record into the students table.

    Parameters:
    db_name (str): The name of the database.
    student_data (tuple): A tuple containing the student's name, age, and grade.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """, student_data)
    conn.commit()
    conn.close()

def fetch_all_students(db_name):
    """
    Retrieves and prints all student records from the students table.

    Parameters:
    db_name (str): The name of the database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    # Define database name
    database_name = "school.db"

    # Create database and students table
    create_database(database_name)

    # Insert sample student data
    insert_student(database_name, ("Qudrat Ullah", 16, "12th Grade"))
    insert_student(database_name, ("Aqeel Ahmad", 17, "12th Grade"))
    insert_student(database_name, ("Amir Abbas", 15, "11th Grade"))

    # Fetch and print all students
    fetch_all_students(database_name)
