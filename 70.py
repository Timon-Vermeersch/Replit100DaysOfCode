#https://www.youtube.com/watch?v=Xrg2XP1JJec&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=117
import dotenv
import os
import time

dotenv_path = ".devcontainer/devcontainer.env"

# Load environment variables from the specified file
dotenv.load_dotenv(dotenv_path)



username_admin = os.environ.get("USERNAME70ADMIN")
password_admin = os.environ.get("PASSWORD70ADMIN")

username = os.environ.get("USERNAME70")
password = os.environ.get("PASSWORD70")

usernames = [username_admin,username]
# print(f"Admin username: {username_admin}, password: {password_admin}")
# print(f"Username: {username}, password: {password}")

usrinp = ""

while usrinp not in usernames:
    print("--LOGIN SCREEN--")
    usrinp = input("Please enter username: ")
    if usrinp == username_admin:
        adminPW = input(f"Please enter PW for {usrinp}: ")
        if adminPW == password_admin:
            print("Acces Granted")
        else:
            print("Acces denied")
    elif usrinp == username:
        usernamePW = input(f"Please enter PW for {usrinp}: ")
        if usernamePW == password:
            print("Acces Granted")
        else:
            print("Acces denied")
    elif usrinp not in usernames:
        print("Username not found")
        time.sleep(1)
        os.system("cls")
