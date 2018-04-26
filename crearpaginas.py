# coding: utf-8

import csv
from csv import DictReader
from slugify import slugify
import yaml

SOURCE = 'static/csv/datos.csv'
DEST = 'content/ponentes/'

dr = DictReader(open(SOURCE))
datos = [d for d in dr]

listado = 'Plenarios Semiplenarios'.split()
ponentes = [d for d in datos if d.get('bloque') in listado]
plantilla = '''---
{}
---
'''

for p in ponentes:
    p = dict(p)
    p['title'] = p.get('nombre')
    p['description'] = p.get('nombre')
    p['keywords'] = ['ponente', 'ponencia', 'congreso', p.get('nombre')]
    p['id'] = 'pagina-ponente'
    p['slug'] = slugify(p['title'].lower())
    dest = '{}{}.md'.format(DEST, p['slug'])
    open(dest, 'w').write(plantilla.format(yaml.dump(p,  default_flow_style=False)))

