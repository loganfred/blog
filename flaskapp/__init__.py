import os
from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

from . import models

db = models.MockDatabase(app.config.get('META_PATH'))

from . import routes
