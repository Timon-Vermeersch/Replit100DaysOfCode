#https://www.youtube.com/watch?v=gogQkRaXPmA
def login():
    print("MY LOGIN SYSTEM")
    print("+++++++++++++++")
    
    accessgranted = "denied"

    while accessgranted == "denied":

        username=input("username: ")
        password=input("password: ")
        
        if username.lower()=="flowxz" and password=="password":
            
            accessgranted = "granted"

        elif username=="louis" and password=="password":
            
            accessgranted = "granted" 
            
        else: 
            print("gtfo")
            accessgranted = "denied"
    print(f"welcome {username}, seems like it's working innit.")
    
    
login()

