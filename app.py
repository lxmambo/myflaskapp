from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from data import Articles
from flask_mysqldb import mySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

#this route is dinamy -> we specify that is going to receive
#a string parameter called id. Type of data and parameter
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#by default routes accept Get request, but for this one we want
#Post to be accepted too, beacuse we are going to send a form data
@app.rout('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm(request.form)

if __name__=="__main__":
    app.run(debug=True)
    # app.debug = True no início
    #teria mesmo efeito.
    #assim conseguimos fazer reload
    #sempre que alterarmos algo