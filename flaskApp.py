
from flask import Flask, render_template, redirect,url_for,request
import sqlite3 
from init_db import init_database

app = Flask(__name__)


init_database()

def get_db_connection():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def hello():
    return render_template('base.html')



@app.route('/name', methods=['POST'])
def process_form():
    
   if(request.method =="POST"): 
        name = request.form['name']
        email = request.form['email']
        con = get_db_connection()
        con.execute('INSERT INTO users (fname, email) VALUES (?,?)',(name,email))
        con.commit()
        con.close()

        return f'The name is: {name} <br/> The email is: {email}'




if __name__ == '__main__':
    app.run(debug=True)