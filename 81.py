#https://www.youtube.com/watch?v=IGZABQUVEu4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=146
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/process' , methods = ['POST'])

def process():
    robot = "You are a robby botto"
    page = "Welcome human"
    form = request.form
    
    print("Keys in form:", form.keys(),list(form.values()))  
    
    # if form["youRobot?"] == "on":
    #     print("FOUND A FKN ROBOT")
    #     return 'found robot'
    
    # elif 'youRobot?' not in form.keys():
    #     print("NOT A FKN ROBOT")
    #     return "Not a robot"

    # if 'youRobot?' not in form.keys():
    #     print("NOT A FKN ROBOT")
    
    try:
        if form["youRobot?"] == "on":
            print("FOUND A FKN ROBOT")
            page = robot
            
    except: 
          print("youRobot not present")

    if form["favFood"] == "sf":
            page = robot
    

    if "error" in form["inf?"]:
            page = robot
    
    return page

@app.route('/')
def index():
    f = open("81.html" , 'r' , encoding= "utf-8")
    page = f.read()
    f.close
    return page

app.run(host = '0.0.0.0', port=81)