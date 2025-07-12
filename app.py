#this is the main app which will show you direction is lost just 
#run (flask run) command and copy paste the url in your browser

from flask import Flask
from flask import render_template
app=Flask(__name__)
from controller import productcontrol
# run the home page to see all the methods
@app.route("/")
def welcome():                                
   return render_template('home.html')          
              
    
    
           