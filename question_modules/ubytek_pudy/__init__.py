# -*- coding: utf-8 -*-
# Zdroj dat
# https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Ciselniky-ISKN/Ciselniky-katastralnich-uzemi-a-pracovist-resortu.aspx
# http://services.cuzk.cz/sestavy/UHDP/...

import sys
sys.path.append("..")
import csv
import os
import random
from utils import location, answer_proposer

path = os.path.dirname(__file__)

def mine_areas(row,rok):
    wanted_areas = 0.0;
    try:
        if rok == '2014':
            for i in [4,5,6,7,8,9]:
                wanted_areas += float(row[i]);
        if rok == '2019':
            for i in [5,7,9,11,13,15]:
                wanted_areas += float(row[i]);            
    except:
        pass
    return(wanted_areas)

KUKOD_2_NUTS = {};
with open(os.path.join(path, 'SC_SEZNAMKUKRA_DOTAZ.csv'), newline='', encoding='cp1250') as csvfile:
    datareader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in datareader:
        try:
            KUKOD_2_NUTS[int(row[7])] = row[3];
        except:
            pass

okresy = location.okresy_name()
data_2014 = {}
data_2019 = {}
data = {}
code_2_name = {}


for okres in okresy:
    okres = location.find_okres(okres)
    if okres:
        code_2_name[okres['cznuts']] = okres['name'];
        data_2014[okres['name']] = 0;
        data_2019[okres['name']] = 0;
        data[okres['name']] = None;


with open(os.path.join(path, 'UHDP-20140101.csv'), newline='', encoding='cp1250') as csvfile:
    datareader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in datareader:
        try:
            data_2014[ code_2_name[ KUKOD_2_NUTS[int(row[0])] ] ] += mine_areas(row,'2014');
        except:
            pass

with open(os.path.join(path, 'UHDP-20190701.csv'), newline='', encoding='cp1250') as csvfile:
    datareader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in datareader:
        try:
            data_2019[ code_2_name[ KUKOD_2_NUTS[int(row[0])] ] ] += mine_areas(row,'2019');
        except:
            pass

for k in data:
    if data_2014[k] > 0.0 and data_2019[k] > 0.0:
        rat = data_2019[k] / data_2014[k]; 
        data[k] = 1.0-rat; 
    

def get_question(okres):
    #===========================================================================
    # try:
    #===========================================================================
    question = answer_proposer.propose_promile_answer(data[okres])
    question['question'] = ('Kolik zemědělsky využívané půdy ubylo za posledních 5 let v okrese '+okres+'?')
    question['source'] = 'www.cuzk.cz/Katastr-nemovitosti/...';
    question['value'] = ('Mezi lety 2014 a 2019 se celková výměra zemědělsky užívané plochy změnila o '+str(1000.0*data[okres])[:5]+' ‰.')
    question['more_html'] = '<div></div>'
    #===========================================================================
    # except:
    #     question = None;
    #===========================================================================
    return question
