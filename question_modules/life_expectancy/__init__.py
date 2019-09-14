# -*- coding: utf-8 -*-
# Zdroj dat
# https://www.czso.cz/csu/czso/nadeje-doziti-v-okresech-a-spravnich-obvodech-orp

import sys
sys.path.append("..")
import csv
import os
import random
from utils import location, answer_proposer

path = os.path.dirname(__file__)
okresy = location.okresy_name()
data = {}


for okres in okresy:
    data[okres] = {'muže': None,
                   'ženy': None};


with open(os.path.join(path, '130140-19data080519.csv'), newline='', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in datareader:
        if row[-1] in okresy and int(row[6])==410045610046000:
            try:
                if int(row[4]) == 1:
                    data[row[-1]]['muže'] = float(row[1])
                elif int(row[4]) == 2:
                    data[row[-1]]['ženy'] = float(row[1])
            except:
                pass
            
def get_question(okres):
    okres = location.find_okres(okres)
    xind = random.randint(0,1)
    gen = ['muže','ženy'][xind]
    living = ['žijícího','žijící'][xind]
    if data[okres['name']][gen]:
        question = answer_proposer.propose_float_answer(data[okres['name']][gen],keep_non_negative=True)
         
        question['question'] = ('Jaká je nadějě dožití (kolik let) '+gen+' ve věku 45 let '+living+' v okrese '+okres['name']+'?')
        question['source'] = 'Naděje dožití v okresech a správních obvodech ORP'
        question['value'] = ('Naděje na dožití je '+str(data[okres['name']][gen])[:4].replace('.',',')+' let.')
        question['more_html'] = '<div></div>'
    else:
        question = None;
 
    return question
