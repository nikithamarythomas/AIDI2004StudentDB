import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('students.db')

# Create a cursor
cur = conn.cursor()

# SQL command to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    amount_due REAL NOT NULL
);
'''

# Execute the SQL command
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Validate table creation
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';")
table_exists = cur.fetchone()

if table_exists:
    print("Table 'students' created successfully.")
else:
    print("Failed to create table 'students'.")

# Close the connection
conn.close()
