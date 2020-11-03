from flask import Flask,render_template, request,url_for,send_from_directory
from PIL import Image
import os

PEOPLE_FOLDER = os.path.join('static', 'pics')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
ALLOWED_EXTENSIONS = ['txt','pdf','png','jpg','jpeg','gif']

@app.route("/")
def hello():
    
    return render_template('home.html',title="Merch")

@app.route('/',methods=['GET','POST'])
def getvalue():
    characters=[]
    database=[]
    meme = ''
    name = request.form['name']
    loweredname = name.lower()
    actualname = loweredname.replace(" ","")
    files = open("memes.txt","r")
    lines = files.readlines()
    for i in lines:
        characters.append(i)
        
    for h in characters:
        a = h.replace("\n",'')
        database.append(a)
        
    if actualname in database:
        match = actualname+" is in the database"
        meme = actualname+'.jpg'
        return render_template('index.html',title="Merch",name=match,database=database,user_image=meme)
    else:
        nomatch = actualname+" is not in the database"
        return render_template('index.html',title="Merch",name=nomatch,database=database,user_image="frowney.jpg")
        
            
    