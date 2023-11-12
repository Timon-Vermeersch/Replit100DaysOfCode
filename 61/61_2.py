import sqlite3 as sq
import datetime

local_db_path = "61\mydatabase.db"
TABLE_NAME = "students"
SELECT_SQL = f"SELECT * FROM {TABLE_NAME} "
INSERT_SQL = f"""INSERT INTO {TABLE_NAME}(id, name, age)
                 VALUES(?, ?, ?)"""

def connect_to_database():
    connection = sq.connect(local_db_path)
    cursor = connection.cursor()
    return connection, cursor

def add_tweet(cursor, tweet):
    print()
    time_now = datetime.datetime.now()
    time_key = f"{time_now.year}{time_now.month}{time_now.day}{time_now.hour}{time_now.minute}{time_now.second}"
    tweet_data = (time_key, tweet, time_now)
    cursor.execute(INSERT_SQL, tweet_data)
    connection.commit()
    return tweet

def view_tweets(cursor):
    print()
    cursor.execute(f"{SELECT_SQL}LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        print()
        for item in row:
            print(item, end=" ")
    print("")

if __name__ == "__main__":
    connection, db_cursor = connect_to_database()

    while True:
        menu = input("1 for add tweet\n2 for show tweets\n>")
        
        if menu == "1":
            tweet_text = input("Enter your tweet: ")
            add_tweet(db_cursor, tweet_text)

        elif menu == "2":
            view_tweets(db_cursor)

        else:
            break  # Exit the loop if an invalid menu option is selected

    connection.close()
