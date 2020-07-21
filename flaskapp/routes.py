from flask import render_template

from . import db
from . import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/articles')
def blog():
    articles = db.articles
    return render_template('blog.html',
                           title='articles',
                           articles=articles)

@app.route('/articles/<int:post>')
def blog_read(post):
    article = db.get_article_by_id(post)
    return render_template('article.html',
                           title=article['title'],
                           article=article)

@app.route('/zettelkasten')
def zettelkasten():
    return render_template('zettelkasten.html', title='zettelkasten')

@app.route('/apis')
def apis():
    return render_template('apis.html', title='apis')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', title='recipes')

@app.route('/todo')
def todo():
    return render_template('todo.html', title='todo')

@app.route('/hiring')
def hiring():
    return render_template('hire_me.html', title='hire me')
