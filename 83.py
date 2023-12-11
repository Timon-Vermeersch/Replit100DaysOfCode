#https://www.youtube.com/watch?v=RTtAk3yFSoY&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=150
from flask import Flask , redirect, render_template, send_file,request
import datetime,os




app = Flask(__name__,static_url_path="/static")
datum = f"{datetime.date.today()}"

@app.route('/', methods = ['GET','POST'])
def home():

    greeting = "hallo"
    date = datum
    entry = "Here is my last blog entry"

    f = open("77_2TemplateHtml.html" , 'r', encoding = "utf-8")
    page = f.read()
    f.close()
    get =  request.args
    if get["style"] == '1':
        page = page.replace("{css}" , "static/css/83_css1.css" )
    else:
        pass
    if get["style"] == "2":
        page = page.replace("{css}" , "static/css/83_css2.css" )
    else:
        pass
    page  = page.replace("{greeting}" , greeting)
    page  = page.replace("{date}" , date)
    page  = page.replace("{entry}" , entry)
    
    return page

@app.route('/portfolio')
def portfolio_page():
    f = open("74.html" , 'r', encoding = "utf-8")
    page = f.read()
    
    
    return page


app.run(host= "0.0.0.0" , port = 81)