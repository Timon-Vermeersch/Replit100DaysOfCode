import sqlite3 as sq
import getpass
import os
import random
import hashlib


##for future: sqlite3 MyFirstDatabase.db "CREATE TABLE diary (date TEXT PRIMARY KEY, entry TEXT NOT NULL);"

TABLE_NAME = "definitlynotpasswords"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME} "

INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(UserId, Salt, HashedPw)
                 VALUES(?, ?, ?)"""

local_db_path = "project71\MySecondDatabase.db"


def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor


def checkUserExistence(uname):
    viewhashSQL = f"SELECT hashedPw,Salt FROM definitlynotpasswords where userId = '{uname}'"
    
    cursor.execute(viewhashSQL)
    uData = cursor.fetchone()


    hashpwd = uData[0]
    hashsalt = uData[1]
    
    if uData:
       
        upw = input("Geef passwoord op AUB: ")
        saltpw = str(hashsalt)+str(upw)
        hashedpw = hashlib.sha256(saltpw.encode()).hexdigest()
        if hashedpw == hashpwd:
            print("gratned")
            connection.close()
            cursor.execute(viewhashSQL)
            

        else:
            print("denied")

        # upw + salt = hash



    else:
        print("notfound")


def addUser(cursor):
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


if __name__ == "__main__":
    connection,cursor = connect_to_database()

    while True:
        print("""1: New User
2: Login""")
        menu = input("> ")
        if menu == "1":
            addUser(cursor)
        elif menu == "2":
            login()
        
    
    





 
    










