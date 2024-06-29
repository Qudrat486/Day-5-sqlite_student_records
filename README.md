# SQLite Database Operations

This project demonstrates basic database operations using SQLite in Python. The script includes functionality to create a database and a table, insert records, and retrieve records from the database.

## Features

- **Create Database**: Creates a new SQLite database and a `students` table with columns: `id`, `name`, `age`, and `grade`.
- **Insert Data**: Adds new student records to the `students` table.
- **Retrieve Data**: Retrieves and prints all student records from the `students` table.

## Requirements

- Python 3.x
- SQLite (included with Python by default)

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sqlite-database-operations.git
cd sqlite-database-operations
```

## Usage

### Create Database and Students Table

The following function creates a new SQLite database and a `students` table:

```python
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
```

### Insert Student Data

The following function inserts a new student record into the `students` table:

```python
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
```

### Retrieve and Print All Student Records

The following function retrieves and prints all student records from the `students` table:

```python
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
```

### Example

The following code demonstrates how to use the functions to create a database, insert sample data, and retrieve all student records:

```python
if __name__ == "__main__":
    # Define database name
    database_name = "school.db"

    # Create database and students table
    create_database(database_name)

    # Insert sample student data
    insert_student(database_name, ("John Doe", 16, "10th Grade"))
    insert_student(database_name, ("Jane Smith", 17, "11th Grade"))
    insert_student(database_name, ("Emily Johnson", 15, "9th Grade"))

    # Fetch and print all students
    fetch_all_students(database_name)
```

### Running the Script

To run the script, execute the following command in your terminal:

```bash
python title_scraper.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
