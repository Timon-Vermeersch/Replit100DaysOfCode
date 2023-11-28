#https://www.youtube.com/watch?v=Xrg2XP1JJec&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=117
import dotenv
import os

dotenv_path = ".devcontainer/devcontainer.env"

# Load environment variables from the specified file
dotenv.load_dotenv(dotenv_path)


username_admin = os.environ.get("USERNAME70ADMIN")
password_admin = os.environ.get("PASSWORD70ADMIN")

username = os.environ.get("USERNAME70")
password = os.environ.get("PASSWORD70")

print(f"Admin username: {username_admin}, password: {password_admin}")
print(f"Username: {username}, password: {password}")