# Zdroj dat
#  CSU

import sys
sys.path.append("..")
import json
import os
from random import randint
from utils import location, answer_proposer, rand

__path__ = os.path.dirname(__file__)

data = [
    {
        "question": "Průměrný věk populace",
        "file": "age.json"
    },
    {
        "question": "Pocit štěstí",
        "file": "pocit_stesti.json"
    },
    {
        "question": "Poměrné míra kouření",
        "file": "smoke.json"
    },
    {
        "question": "Spokojenost ve vztahu",
        "file": "vztah_spokojenost.json"
    },
    {
        "question": "Spokojenost v zaměstnání",
        "file": "zamestnani_spokojenost.json"
    },
    {
        "question": "Spokojenost se životem",
        "file": "zivot_spokojenost.json"
    },
]

def load_data():
    for db in data:
        db['data'] = json.load(open(os.path.join(__path__, db['file'])))


load_data()


def get_question(okres):
    okres = location.find_okres(okres)

    i = randint(0, len(data)-1)

    db = data[i]

    value = db['data'][okres['cznuts']]

    question = answer_proposer.propose_percentage_answer(value*0.01)

    question['question'] = db['question'] + ' v okrese?'
    question['source'] = 'ČSÚ - Souhrnná data o České republice'
    question['value'] = '{} %'.format(value)
    question['more_html'] = '<div></div>'

    return question
