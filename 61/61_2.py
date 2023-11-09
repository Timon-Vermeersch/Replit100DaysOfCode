import sqlite3 as sq,datetime
##obj = 1 person twitter ww
#1 add tweets = datetime.datetime.now() = key

#2 view tweets timestamp -  show in reverse chrono - 10per


local_db_path = "61\mydatabase.db"
connection = sq.connect(local_db_path)
db_cursor = connection.cursor()

sql = """INSERT INTO students(id, name, age)
VALUES(?, ?, ?)"""

select_sql = "SELECT * FROM students "
db_cursor.execute(select_sql) 





def addTweet():
    print()
    tweet = input("uw tweet: ")

    tijd = datetime.datetime.now()
    timekey = (f"{tijd.year}{tijd.month}{tijd.day}{tijd.hour}{tijd.minute}{tijd.second}")

    dude = (timekey, tweet, tijd) 
    db_cursor.execute(sql,dude)

    connection.commit()
    connection.close()
    
    return tweet
def viewTweets():
    print()


while True:
    menu = input("1 for add tweet\n2 for show tweets\n>")
    if menu == "1":
        tweet = addTweet()
        
        

        
        
    if menu == "2":
        viewTweets()

