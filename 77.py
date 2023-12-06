#https://www.youtube.com/watch?v=QER5PelRPm0&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=131
from flask import Flask , redirect
app = Flask(__name__,static_url_path="/static")

@app.route('/houdini')
def portfolio():
    return redirect("https://www.youtube.com/watch?v=YIvwCIwDQT8&list=RDYIvwCIwDQT8&start_radio=1")

@app.route('/')
def index():
    myName = "Anya Forger"
    title = "The pinkest nerd"
    f = open("75.html",'r',encoding='utf-8')
    page = f.read()
    f.close()
    page = page.replace("{myName}", myName)
    page = page.replace("{title}", title)
    return page

app.run(host = '0.0.0.0', port=81)