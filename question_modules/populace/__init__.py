# -*- coding: utf-8 -*-
# Zdroj dat
#  https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&z=T&f=TABULKA&ds=ds2287&pvo=DEM07D&katalog=31737&c=v741%7E8__RP2017&str=v741#w=
#
import sys
sys.path.append("..")
import csv
import os
from utils import location, answer_proposer

path = os.path.dirname(__file__)

okresy = location.okresy_name()

data = {}

with open(os.path.join(path, 'DEM07D.csv'), newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    data = {}
    for row in datareader:
        if row[1] in okresy:
            data[row[1]] = {
                'narozeni': int(row[2]),
                'kluci': int(row[3]),
                'holky': int(row[4]),
                'prvorodicka_prum_vek': float(row[10])
            }

def get_question(okres):
    row = data[okres]

    question = answer_proposer.propose_integer_answer(row['narozeni'])

    question['question'] = 'Kolk dětí se narodilo v roce 2017?'
    question['source'] = 'ČSÚ - Souhrnná data o České republice'
    question['value'] = '{narozeni} z toho {holky} holčiček a {kluci} kluků'.format(**row)
    question['more_html'] = '<div></div>'

    return question
