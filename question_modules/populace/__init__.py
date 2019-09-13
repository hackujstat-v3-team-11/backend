# -*- coding: utf-8 -*-
# Zdroj dat
#  https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&z=T&f=TABULKA&ds=ds2287&pvo=DEM07D&katalog=31737&c=v741%7E8__RP2017&str=v741#w=
#
import sys
sys.path.append("..")
import csv
import os
from utils import location

path = os.path.dirname(__file__)

okresy = location.okresy_name()

data = {}

with open(os.path.join(path, 'DEM07D.csv'), newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    data = {}
    for row in datareader:
        if row[1] in okresy:
            data[row[1]] = {
                'narozeni': row[2],
                'kluci': row[3],
                'holky': row[4],
                'prvorodicka_prum_vek': row[10]
            }

def get_question(okres):
    row = data[okres]

    return {
        'question': 'Kolik dětí se narodilo v roce 2017?',
        'answers': [
            'A: 0 - 10',
            'B: 10 - 20',
            'C: 20 - 30',
            'D: 30 - 40'
        ],
        'corrects': 1,
        'source': 'ČSÚ - Souhrnná data o České republice',
        'value': row['narozeni'] + ' z toho ' + row['holky'] + ' holčiček a ' + row['kluci'] + ' kluků',
        'more_html': '<div></div>'
    }
