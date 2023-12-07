#https://www.youtube.com/watch?v=y-Gd0B-GOnM&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=133
from flask import Flask

app = Flask(__name__)

@app.route('/<pageNumber>')

def index(pageNumber):

    reflection = {}
    reflection = {key: ['placeholder', 'placeholder'] for key in range(101)}
    reflection[77][0] = "77 was cool net zoals frederic"
    reflection[77][1] = "https://github.com/YOLOTANKERSWAG2023/Replit100DaysOfCode/blob/main/77.py"
    
    reflection[78][0] = ".replace(text , reflection[int(pageNumber)][1]) was tricky for some reason idk, lmao ge dacht dat deze string een bug was e hihi"
    reflection[78][1] = "https://github.com/YOLOTANKERSWAG2023/Replit100DaysOfCode/blob/main/78.py"
    
    f = open("78.html" , 'r' , encoding='utf-8')
    page = f.read()
    #prevnr
    prevNummer = int(pageNumber)
    prevNummer-=1
    page = page.replace("{prevNummer}" , str(prevNummer))
    #nextnr
    nextNummer = int(pageNumber)
    nextNummer+=1
    page = page.replace("{nextNummer}" , str(nextNummer))

    #change titel
    page = page.replace("{day}" , pageNumber)

    #change link
    page = page.replace("{link}" ,  reflection[int(pageNumber)][1])

    #change entry
    try:
        page = page.replace("{entry}", reflection[int(pageNumber)][0])
    except KeyError:
        page = page.replace("{entry}", 'placeholder')
    
     

    return page
    
    




app.run(host = '0.0.0.0' , port = 81)
