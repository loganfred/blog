import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    ARTICLE_SOURCE_DIRECTORY = os.path.join(basedir,
                                            'flaskapp',
                                            'articles',
                                            'src')

    STATIC_IMAGES_DIRECTORY = os.path.join(basedir,
                                           'flaskapp',
                                           'static',
                                           'assets')

