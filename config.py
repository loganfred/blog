import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    META_PATH = os.path.join(basedir,
                             'flaskapp',
                             'templates',
                             'content',
                             'meta')

    STATIC_IMAGES_DIRECTORY = os.path.join(basedir,
                                           'flaskapp',
                                           'static',
                                           'assets')
