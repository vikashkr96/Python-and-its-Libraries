import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"  
)
cursor = conn.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    branch VARCHAR(50)
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, age, branch) VALUES ('Amit', 20, 'CSE')")
conn.commit()

# Retrieve and display data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()

