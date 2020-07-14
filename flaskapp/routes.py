from flask import render_template
import re
import os

from . import app

# helper functions

article_path = os.path.join(os.path.dirname(__file__), 'articles')

def findTitle(article):
    title = re.compile('<h1.*>(.*)</h1>', re.DOTALL)
    try:
        match = title.match(article).groups(1)[0]
        return match
    except AttributeError:
        return None


def searchContent(location):
    articles = {}
    files = [x for x in os.listdir(location) if '.html' in x]
    for num, file in enumerate(files):
        text = open(os.path.join(location, file), 'r').read(250)
        title = findTitle(text)
        articles[num] = {'path':file, 'title':title}
    return articles

@app.route('/')
@app.route('/index')
def index():
    articles = searchContent(article_path)
    return render_template('blog.html',
                           title='Blog',
                           articles=articles)

@app.route('/article/<post>')
def blog_read(post):
    folder = os.path.join(article_path, post)
    with open(folder, 'r') as f:
        article = f.read()
    return render_template('article.html',
                           title='Article',
                           post=article)

@app.route('/hireme')
def career():
    return render_template('career.html', title='Hire Me')
