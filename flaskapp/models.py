import shutil
import os
from bs4 import BeautifulSoup

from . import app

class Database:

    def __init__(self, path):

        self.files = self.get_html_files(path)
        self.articles = []

        for id, file in enumerate(self.files):

            parsed = self.parse(file)

            self.articles.append(dict(id=id, file=file, **parsed))

    def get_html_files(self, location):
        return [os.path.join(location, f) for f in os.listdir(location) if '.html' in f]


    def parse(self, name):


        a = self.import_images(name)

        p = BeautifulSoup(open(name, 'r'), 'html.parser')

        md = {t.get('name'): t.get('content') for t in p.find_all('meta') if t.get('name') is not None}

        c = '\n'.join([tag.prettify() for tag in p.find('head').findChildren(recursive=False)])

        t = p.title.string

        d = p.find_all('p', 'date')[0].string

        c = '\n'.join([tag.prettify() for tag in p.find('body').findChildren(recursive=False)])

        m = '\n'.join([tag.prettify() for tag in p.find_all('meta')])

        s = '\n'.join([tag.prettify() for tag in p('p', class_=None) ])[:200]+'...'

        html = p.prettify(formatter='html')

        return dict(html=html, preview=s, date=d, meta=m, title=t, content=c, assets=a, **md)

    def get_article_by_id(self, id):
        return self.articles[id]

    def import_images(self, file):

        p = BeautifulSoup(open(file, 'r'), 'html.parser')

        src_path = app.config['ARTICLE_SOURCE_DIRECTORY']
        static_path = app.config['STATIC_IMAGES_DIRECTORY']

        if len(p.find_all('img')) == 0:
            return dict()
        else:
            assets = {}
            for tag in p.find_all('img'):
                if not 'static' in tag['src']:
                    shutil.copy(os.path.join(src_path, tag['src']),
                                os.path.join(static_path, os.path.basename(tag['src'])))
                    tag['src'] = tag['src'].replace('assets', '/static/assets')
                assets.update({os.path.basename(tag['src']): tag['src']})

            with open(file, 'w') as f:
                f.write(p.prettify())

            return assets

    def print(self):
        for article in self.articles:
            for key in article.keys():
                print('\n', key, ':\n')
                print(article[key])
                print()

