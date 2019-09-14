# -*- coding: utf-8 -*-
# Zdroj dat
# https://opendata.mzcr.cz/dataset/nrpzs/resource/9c499739-f924-4c28-a295-118c433712e8

import sys
sys.path.append("..")
import csv
import os
import random
from utils import location, answer_proposer

path = os.path.dirname(__file__)
kraje = location.kraje_name()

data = {}
code_2_name = {}

for kraj in kraje:
    kraj = location.find_kraj(kraj)
    if kraj:
        code_2_name[kraj['cznuts']] = kraj['name'];
        data[kraj['name']] = 0;

with open(os.path.join(path, 'narodni-registr-poskytovatelu-zdravotnich-sluzeb.csv'), newline='', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in datareader:
        if row[10] in code_2_name:
            data[code_2_name[row[10]]] += 1;

            
def get_question(okres):
    kraj = location.get_kraj(okres)
    #===========================================================================
    # try:
    #===========================================================================
    print(kraj.keys())
    question = answer_proposer.propose_integer_answer(data[kraj['name']],keep_non_negative=True)
     
    question['question'] = ('O kolika zdravotnických pracovištích '+kraj['inflection']+' víme?')
    question['source'] = 'narodni-registr-poskytovatelu-zdravotnich-sluzeb.csv';
    question['value'] = (kraj['inflection'].capitalize()+' víme o '+str(data[kraj['name']])+' zdravotnických pracovištích.')
    question['more_html'] = '<div></div>'
    #===========================================================================
    # except:
    #     question = None;
    #===========================================================================
    return question
