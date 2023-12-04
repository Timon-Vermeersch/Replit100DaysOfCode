#https://www.youtube.com/watch?v=hyNIcmTi7lU&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=121
import sqlite3 as sq
import datetime, os, random, hashlib


TABLE_NAME_DIARY = "diary"
SELECT_SQL_DIARY = f"SELECT * FROM {TABLE_NAME_DIARY} "
INSERT_SQL_DIARY = f"""INSERT INTO {TABLE_NAME_DIARY}(date, entry)
                 VALUES(?, ?)"""

TABLE_NAME = "user"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME} "
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(userId, Salt, HashedPw)
                 VALUES(?, ?, ?)"""

local_db_path = "project72\encrypteddiary.db"

def checkFirstStart(cursor):
    cursor.execute("""
        SELECT CASE
            WHEN EXISTS (SELECT 1 FROM user)
            THEN 0
            ELSE 1
        END;
    """)
    result = cursor.fetchone()
    return  bool(result[0])

def checkUserExistence(uname):
    viewhashSQL = f"SELECT hashedPw,Salt FROM user where userId = '{uname}'"
    
    cursor.execute(viewhashSQL)
    uData = cursor.fetchone()


    
    
    if uData:
        hashpwd = uData[0]
        hashsalt = uData[1]
       
        upw = input("Geef passwoord op AUB: ")
        saltpw = str(hashsalt)+str(upw)
        hashedpw = hashlib.sha256(saltpw.encode()).hexdigest()
        if hashedpw == hashpwd:
            print("gratned")
            
            
            

        else:
            print("denied")

        # upw + salt = hash



    else:
        print("notfound")

def createUser():
    print("--Adding new user--")
    uid = input("Pls give me ur name: ")
    upw = input("please enter a pw: ")
    rsalt = random.randint(10000,99999)
    saltpw = str(rsalt)+str(upw)
    hashedpw = hashlib.sha256(saltpw.encode()).hexdigest()
    data = (uid, rsalt , hashedpw)
    cursor.execute(INSERT_SQL, data)
    connection.commit()

def login(): 
    print("--Logging in--")
    uname = input("please enter username: ")
    checkUserExistence(uname)

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

def add_entry(cursor, entryText):
    print()
    time_now = datetime.datetime.now()
    time_key = f"{time_now.year}-{time_now.month}-{time_now.day}-{time_now.hour}:{time_now.minute}"
    entry = (time_key, entryText)
    cursor.execute(INSERT_SQL_DIARY, entry)
    connection.commit()

def view_diary(cursor):
    os.system("cls")
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME_DIARY};")
    count_result = cursor.fetchone()
    count = count_result[0]
    offset = count
    offset-=1

    while offset >= 0:
        os.system("cls")
        print()
        cursor.execute(f"{SELECT_SQL_DIARY}LIMIT 1 OFFSET {offset}")
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

def menu():
    while True:
            menu = input("1 for add entry\n2 for show last entry\n>")
            if menu == "1":
                entryText = input("Enter your diary text: ")
                add_entry(cursor,entryText)
            elif menu == "2":
                view_diary(cursor)
            elif menu == "q":
                 connection.close()
                 quit()

if __name__ == "__main__":
    connection,cursor = connect_to_database()
    if checkFirstStart(cursor):
        createUser()
    else:
        login()
        print("continue to menu")
        menu()