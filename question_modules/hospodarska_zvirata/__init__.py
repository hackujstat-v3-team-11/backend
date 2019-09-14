#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Zdroj dat
#  https://www.czso.cz/csu/czso/hospodarska-zvirata-podle-kraju
#
import sys
sys.path.append("..")
import csv
import os
import pprint
import random
from utils import location, answer_proposer, rand

__path__ = os.path.dirname(__file__)

okresy = location.okresy_name()

data = {}
with open(os.path.join(__path__, '270230-19data053119.csv'), newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        uzemi = row['uzemi_txt']
        zvire = row['DRUHZVIRE_txt']
        rok = row['rok']
        pocet = row['hodnota']

        if not uzemi in data:
            data[uzemi] = {}
        if not zvire in data[uzemi]:
            data[uzemi][zvire] = { "max_rok": rok }
        if not rok in data[uzemi][zvire]:
            data[uzemi][zvire][rok] = {}
        if not pocet in data[uzemi][zvire][rok]:
            data[uzemi][zvire][rok] = pocet

        max_rok = data[uzemi][zvire]["max_rok"]
        if  data[uzemi][zvire][max_rok] < pocet:
            data[uzemi][zvire]["max_rok"] = rok 


lut = {'Drůbež': 'drůbeže',
 'Koně': 'koní',
 'Kozy': 'koz',
 'Krávy': 'krav',
 'Ovce': 'ovcí',
 'Prasata': 'prasat',
 'Prasnice chovné': 'chovných prasnic',
 'Skot': 'skotu',
 'Slepice': 'slepic'}


def get_question(okres):

    kraj = location.get_kraj(okres)
    row = data[kraj['name']]

    zvire = rand.get_key(row)

    rok = rand.get_key(row[zvire])

    pocet = row[zvire][rok]

    question = answer_proposer.propose_integer_answer(int(row[zvire][rok]))

    question['question'] = 'Kolik se {} chovalo {} v roce {}?'.format(kraj['inflection'],lut.get(zvire, zvire), rok)
    question['source'] = 'ČSÚ - Hospodářská zvířata podle krajů'
    question['value'] = '{} kusů {}'.format(pocet, lut.get(zvire, zvire))
    question['more_html'] = '<div></div>'

    return question

if __name__ == "__main__":
    print(get_question('Liberec'))