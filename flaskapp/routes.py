from flask import send_from_directory
from flask import render_template
import os

from . import app
from . import db
from .models import meta_from_dict

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/writings/')
def writings():

    template = os.path.join('content', 'writings', 'index.html')

    return render_template(template)

@app.route('/writings/<path:path>')
def writing(path):

    template = os.path.join('content', 'writings', path)

    return render_template(template)

@app.route('/zk/')
def zettelkastens():
    template = os.path.join('content', 'zettelkasten', 'index.html')

    return render_template(template)

@app.route('/zk/<path:path>')
def zettelkasten(path):
    template = os.path.join('content', 'zettelkasten', path)

    return render_template(template)

@app.route('/recipes/')
def recipes():

    template = os.path.join('content', 'recipes', 'index.html')

    return render_template(template)

@app.route('/recipes/<path:path>')
def recipe(path):

    template = os.path.join('content', 'recipes', path)

    return render_template(template)

@app.route('/api')
def apis():
    return render_template('apis.html')


@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/hiring')
def hiring():
    return render_template('hireme.html')

@app.route('/about')
def about():
    return render_template('about.html')
