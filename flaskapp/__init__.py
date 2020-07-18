import os
from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

from . import models

db = models.Database(os.path.join(os.path.dirname(__file__), 'articles'))

from . import routes
