import sqlite3

# Path to the SQLite database file
database_path = 'employees.db'

# Create a connection to the database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Create the employees table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        position TEXT
    )
''')

# Insert sample data into the employees table
employees_data = [
    (1, 'Bindya Philip', 23, 'Manager'),
    (2, 'Tusimirwe Jemily', 28, 'Developer'),
    (3, 'Semaganda Trevour', 25, 'Salesperson')
]

cursor.executemany('''
    INSERT INTO employees (id, name, age, position)
    VALUES (?, ?, ?, ?)
''', employees_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")
