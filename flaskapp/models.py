import warnings
import json
import os


def meta_from_dict(self, d):

    meta = ''

    author = d.get('author')
    keywords = d.get('keywords')
    description =  d.get('description')

    if author:
        meta += f'<meta name="author" content="{author}">\n'
    if keywords:
        meta += f'<meta name="keywords" content="{", ".join(keywords)}">\n'
    if description:
        meta += f'<meta name="description" content="{description}">\n'

    return meta


class MockDatabase:

    def __init__(self, path):

        for key, val in self._compile_meta(path).items():
            setattr(self, key, val)

    def _compile_meta(self, path):

        dictionary = {}

        for r, _, fs in os.walk(path):

            folder = os.path.basename(r)

            if folder == 'meta':
                continue

            metas = []
            for f in fs:
                metas.append(json.load(open(os.path.join(r, f))))

            dictionary[folder] = metas

        return dictionary

    def get_article_from_title(self, title):

        lst_cmp = [x for x in self.writings if x.get('title') == title]

        if len(lst_cmp) < 1:
            return None
        else:
            return lst_cmp[0]
