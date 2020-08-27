from flask import Flask, render_template
from data import Articles

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

if __name__=="__main__":
    app.run(debug=True)
    # app.debug = True no início
    #teria mesmo efeito.
    #assim conseguimos fazer reload
    #sempre que alterarmos algo