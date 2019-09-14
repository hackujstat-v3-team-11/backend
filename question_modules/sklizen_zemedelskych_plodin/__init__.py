# -*- coding: utf-8 -*-
# Zdroj dat
#  https://www.czso.cz/csu/czso/sklizen-zemedelskych-plodin-podle-kraju
#
import sys
sys.path.append("..")
import csv
import os
from utils import location, answer_proposer, rand
from random import randint

__path__ = os.path.dirname(__file__)


def load_data():
    kraje = location.kraje_name()

    data = {}
    kod = {}

    with open(os.path.join(__path__, '270229-19data043019.csv'), newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = {}
        for row in datareader:
            kod[row[2]] = 1

            if not row[11] in kraje:
                continue

            if row[2] != '5906':
                continue

            if not row[11] in data:
                data[row[11]] = {}

            if not row[7] in data[row[11]]:
                data[row[11]][row[7]] = {}

            if not row[12] in data[row[11]][row[7]]:
                data[row[11]][row[7]][row[12]] = float(row[1])
    return data

data = load_data()


lut = {'Brambory': 'brambor',
'Cukrovka technická': 'technické cukrovky',
'Ječmen': 'ječmene',
'Kukuřice na zeleno a siláž': 'kukuřice na zeleno a siláž',
'Luskoviny na zrno (hrách setý, lupina, bob, fazol, jiné luskoviny)': 'luskoviny na zrno',
'Obiloviny na zrno (pšenice, žito, ječmen, oves, tritikale, kukuřice na zrno, směsky obilovin jarní, směsky obilovin ozimé, čirok, jiné obiloviny)': 'obilovin na zrno',
'Pícniny na orné půdě': 'pícnin na orné půdě',
'Pšenice': 'pšenice',
'Trvalé travní porosty': 'trvalého travního porostu',
'Řepka': 'řepka',
'Žito': 'žita'}


def get_question(okres):
    kraj = location.get_kraj(okres)

    row = data[kraj['name']]

    rok = rand.get_key(row)

    plodina = rand.get_key(row[rok])

    question = answer_proposer.propose_integer_answer(int(row[rok][plodina]))

    question['question'] = 'Kolik tun {} se vypěstovalo v roce {} {}'.format(lut.get(plodina, plodina), rok, kraj['inflection'])
    question['source'] = 'ČSÚ - Sklizeň zemědělských plodin podle krajů'
    question['value'] = '{} tun {}'.format(row[rok][plodina], plodina)
    question['more_html'] = '<div></div>'

    return question
