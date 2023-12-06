from flask import Flask , redirect, render_template, send_file
import datetime,os




app = Flask(__name__,static_url_path="/static")
datum = f"{datetime.date.today()}"

@app.route('/')
def home():

    greeting = "hallo"
    date = datum
    entry = "Here is my last blog entry"

    f = open("77_2TemplateHtml.html" , 'r', encoding = "utf-8")
    page = f.read()
    f.close()

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