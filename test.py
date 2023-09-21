import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

# resets preexisting tables if they exist (only need during testing)
cur.execute('DROP TABLE IF EXISTS Staff')

# creates staff table
cur.execute('''
     CREATE TABLE Staff (
          staff_Id int NOT_NULL AUTOINCREMENT PRIMARY KEY, 
          job_Id FOREIGN KEY, 
          bio VARCHAR(500),
          hobbies VARCHAR(500),
          birthday DATE,
          picture VARCHAR(500),
     )       
''')
# creates projects table
cur.execute(''' 
     CREATE TABLE Projects (
          project_Id int NOT_NULL AUTOINCREMENT PRIMARY KEY, 
          name VARCHAR(50), 
          description VARCHAR(500),
          status VARCHAR(50),
          job_Id FOREIGN KEY
     )
''')
# creates jobs table
cur.execute('''
     CREATE TABLE Jobs (
          job_Id int NOT_NULL AUTOINCREMENT PRIMARY KEY,
          job_Title VARCHAR(50),
          job_Description VARCHAR(500),
     ) 
''')

