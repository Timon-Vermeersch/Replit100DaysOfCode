import sqlite3 as sq
import datetime
import getpass
import os
##for future: sqlite3 MyFirstDatabase.db "CREATE TABLE diary (date TEXT PRIMARY KEY, entry TEXT NOT NULL);"
TABLE_NAME = "diary"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME} "
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(date, entry)
                 VALUES(?, ?)"""


local_db_path = "62_Diary\MyFirstDatabase.db"
wachtwoord = "123"

def checkpw():
    ww = getpass.getpass("pls enter password: ")
    if ww == "123":
        os.system("cls")
        return True

    else:
        return False
    
def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

def add_entry(cursor, entryText):
    print()
    time_now = datetime.datetime.now()
    time_key = f"{time_now.year}-{time_now.month}-{time_now.day}-{time_now.hour}:{time_now.minute}"
    entry = (time_key, entryText)
    cursor.execute(INSERT_SQL, entry)
    connection.commit()

def view_diary(cursor):
    os.system("cls")
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME};")
    count_result = cursor.fetchone()
    count = count_result[0]
    offset = count
    offset-=1

    while offset >= 0:
        os.system("cls")
        print()
        cursor.execute(f"{SELECT_SQL}LIMIT 1 OFFSET {offset}")
        rows = cursor.fetchall()
        for row in rows:
            for item in row:
                    print(item, end=" ")
                    print("\n")

        offsetincrease= input("\nq to go to menu, '+' for show nxt entry '-' for show previous entry\n:  ")
        if offsetincrease == "+":
                offset += 1
        else: offset-= 1

        if offsetincrease == "q":
             break


    offset = 0   
    



if __name__ == "__main__":
    connection , cursor = connect_to_database()
    os.system("cls")
    if checkpw():
        print("Access granted!")
        print("\n")
        while True:
            menu = input("1 for add entry\n2 for show last entry\n>")
            if menu == "1":
                entryText = input("Enter your diary text: ")
                add_entry(cursor,entryText)
            elif menu == "2":
                view_diary(cursor)
    else:
        print("Acces denied!")
