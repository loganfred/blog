from bs4 import BeautifulSoup
import shutil
import glob
import os

from . import app

class Parser:

    def __init__(self, folder_path):

        basepath = os.path.dirname(__file__)

        self.parse_folder(os.path.join(basepath, folder_path))

    def parse_folder(self, dir_path):

        self.results = []

        for i, f in enumerate(glob.glob(os.path.join(dir_path, '*.html'))):
            result = self.parse(f)
            result.update(dict(id=i, file=f))
            self.results.append(result)

    def parse(self, file_path):
        pass

class ArticleParser(Parser):

    def parse(self, file_path):

        a = self.import_images(file_path)
        p = BeautifulSoup(open(file_path, 'r'), 'html.parser')
        md = {t.get('name'): t.get('content') for t in p.find_all('meta') if t.get('name') is not None}
        c = '\n'.join([tag.prettify() for tag in p.find('head').findChildren(recursive=False)])
        t = p.title.string
        d = p.find_all('p', 'date')[0].string
        c = '\n'.join([tag.prettify() for tag in p.find('body').findChildren(recursive=False)])
        m = '\n'.join([tag.prettify() for tag in p.find_all('meta')])
        s = '\n'.join([tag.prettify() for tag in p('p', class_=None) ])[:200]+'...'

        html = p.prettify(formatter='html')

        return dict(html=html, preview=s, date=d, meta=m, title=t, content=c, assets=a, **md)

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

class RecipeParser(Parser):

    def parse(self, file_path):

        p = BeautifulSoup(open(file_path, 'r'), 'html.parser')
        md = {t.get('name'): t.get('content') for t in p.find_all('meta') if t.get('name') is not None}
        c = '\n'.join([tag.prettify() for tag in p.find('head').findChildren(recursive=False)])
        t = p.title.string
        d = p.find_all('p', 'date')[0].string
        c = '\n'.join([tag.prettify() for tag in p.find('body').findChildren(recursive=False)])
        m = '\n'.join([tag.prettify() for tag in p.find_all('meta')])
        s = '\n'.join([tag.prettify() for tag in p('p', class_=None) ])[:200]+'...'

        html = p.prettify(formatter='html')

        return dict(html=html, preview=s, date=d, meta=m, title=t, content=c, **md)

class ZettelkastenParser(Parser):

    def parse(self, file_path):

        p = BeautifulSoup(open(file_path, 'r'), 'html.parser')
        md = {t.get('name'): t.get('content') for t in p.find_all('meta') if t.get('name') is not None}
        c = '\n'.join([tag.prettify() for tag in p.find('head').findChildren(recursive=False)])
        t = p.title.string
        d = p.find_all('p', 'date')[0].string
        c = '\n'.join([tag.prettify() for tag in p.find('body').findChildren(recursive=False)])
        m = '\n'.join([tag.prettify() for tag in p.find_all('meta')])
        s = '\n'.join([tag.prettify() for tag in p('p', class_=None) ])[:200]+'...'

        html = p.prettify(formatter='html')

        return dict(html=html, preview=s, date=d, meta=m, title=t, content=c, assets=a, **md)

class TodoParser(Parser):

    def parse(self, file_path):

        p = BeautifulSoup(open(file_path, 'r'), 'html.parser')

        md = {t.get('name'): t.get('content') for t in p.find_all('meta') if t.get('name') is not None}
        items = [tag.string for tag in p('li')]

        return dict(items=items, **md)


class Database:

    def __init__(self):


        #import pdb; pdb.set_trace()

        ar = ArticleParser('articles')
        zk = ZettelkastenParser('zettelkasten')
        td = TodoParser('todo')
        rp = RecipeParser('recipes')

        self.articles = ar.results
        self.zks = zk.results
        self.todo = td.results[0]
        self.recipes = rp.results
