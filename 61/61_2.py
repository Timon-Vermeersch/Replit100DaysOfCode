import sqlite3 as sq

local_db_path = "61\mydatabase.db"
connection = sq.connect(local_db_path)
db_cursor = connection.cursor()

dude = (34, "xdxp", 45)  # Removed the extra backslash

sql = """INSERT INTO students(id, name, age)
VALUES(?, ?, ?)"""

# create_table_sql = '''
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER,
#     name TEXT,
#     age INTEGER
# );
# '''

# rwar
#db_cursor.execute(create_table_sql)
select_sql = "SELECT * FROM students "
db_cursor.execute(select_sql) 

db_cursor.execute(sql,dude)

connection.commit()
connection.close()
