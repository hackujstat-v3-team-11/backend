# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import json
import os
import random

path = os.path.dirname(__file__)

with open(os.path.join(path, 'jokes.json'), encoding='utf-8') as jsnf:
    data = json.load(jsnf)

def get_question(okres,reduction_factor=0.15):
    if random.random() <= reduction_factor:
        Q = data[random.randint(0,len(data)-1)]
        question = {
            'answers': Q['answers'],
            'correct': Q['correct'],
            'question': Q['question'],
            'source': '',
            'value': Q['value'],
            'more_html': Q['more_html']  }
    else:
        question = None;
    return question
