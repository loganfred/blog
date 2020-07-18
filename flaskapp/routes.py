from flask import render_template

from . import db
from . import app

@app.route('/')
@app.route('/index')
def index():
    articles = db.articles
    return render_template('blog.html',
                           title='Blog',
                           articles=articles)

@app.route('/article/<int:post>')
def blog_read(post):
    article = db.get_article_by_id(post)
    return render_template('article.html',
                           title='Article',
                           article=article)

@app.route('/hireme')
def career():
    return render_template('career.html', title='Hire Me')
