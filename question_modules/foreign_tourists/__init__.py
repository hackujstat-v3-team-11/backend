# -*- coding: utf-8 -*-
# Zdroj dat
# https://www.czso.cz/csu/czso/hoste-a-prenocovani-v-hromadnych-ubytovacich-zarizenich-podle-zemi

import sys
sys.path.append("..")
import csv
import os
import random
from utils import location, answer_proposer

path = os.path.dirname(__file__)
kraje = location.kraje_name()
data = {}
mesice = ['','lednu','únoru','březnu','dubnu','květnu','červnu',
          'červenci','srpnu','září','říjnu','listopadu','prosinci']

for kraj in kraje:
    data[kraj] = [];

with open(os.path.join(path, '020063-19data080819.csv'), newline='', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in datareader:
        if row[14] in kraje and int(row[3])==2654: 
            data[row[14]].append( {
                'rok': int(row[10]),
                'mesic': int(row[11]),
                'zeme_puvodu': row[9],
                'pocet': int(row[1])
            } )

def get_question(okres):
    kraj = location.get_kraj(okres)
    dta = data[kraj['name']];
    if len(dta) > 0:
        zaznam = dta[random.randint(0,len(dta)-1)];
        question = answer_proposer.propose_integer_answer(zaznam['pocet'],keep_non_negative=True)
        
        question['question'] = ('Kolik turistů ze země '+zaznam['zeme_puvodu']+' přespalo v '+
            mesice[zaznam['mesic']]+' '+str(zaznam['rok'])+' '+kraj['inflection']+'?')
        question['source'] = 'ČSÚ a CzechTourism - Souhrnná data o České republice'
        question['value'] = ('Turistů z '+zaznam['zeme_puvodu']+' přespalo v '+mesice[zaznam['mesic']]+' '+
            str(zaznam['rok'])+' '+kraj['inflection']+' '+str(zaznam['pocet'])+'.')
        question['more_html'] = '<div></div>'
    else:
        question = None;

    return question
