# -*- coding: utf-8 -*-
# data gathered from EOCD open data portal and pre-filtered

import sys
sys.path.append("..")
import json
import os
import random
from utils import answer_proposer

path = os.path.dirname(__file__)

with open(os.path.join(path, 'GDP.json'), encoding='utf-8') as jsnf:
    data = json.load(jsnf)
    roky = list(data.keys())

def get_question(okres,reduction_factor=0.15):
    if random.random() <= reduction_factor:
        try:
            Q = random.randint(0,2)
            year = roky[random.randint(0,len(roky)-1)]
            ydta = data[year]
            
            if Q == 0:
                cdta = ydta[list(ydta.keys())[random.randint(0,len(ydta.keys())-1)]]
                HDP,ccode,ceng,cczech,popul = cdta; del(ccode,ceng);
                GDP_H = int(HDP/popul)
                
                question = answer_proposer.propose_integer_answer(GDP_H,keep_non_negative=True)
                
                question['question'] = ('Jaký byl hrubý domácí produkt (HDP) v dolarech (USD) na obyvatele ve státě '+cczech+' v roce '+str(year)+'?',)
                question['source'] = 'aggregated OECD data'
                question['value'] = (cczech+' ('+str(year)+'):\r'+
                                     'populace: '+str(popul)+'\r'+
                                     'HDP: '+str(HDP))
                question['more_html'] = 'https://data.oecd.org'
                
            else:
                countries = list(ydta.keys());
                if len(countries) > 4:
                    chosen = [];
                    for i in range(4):
                        x = random.randint(0,len(countries)-1)
                        chosen.append(ydta[countries[x]])
                        del(countries[x])
    
                    HDP_a = int(chosen[0][0]/chosen[0][4]);
                    name_a = chosen[0][3];
                    HDP_b = int(chosen[1][0]/chosen[1][4]);
                    name_b = chosen[1][3];
                    HDP_c = int(chosen[2][0]/chosen[2][4]);
                    name_c = chosen[2][3];
                    HDP_d = int(chosen[3][0]/chosen[3][4]);
                    name_d = chosen[3][3];
                    
                    
                    hdps = [HDP_a,HDP_b,HDP_c,HDP_d]
                    if Q == 1:
                        slovo = 'nejmenší'
                        resp = hdps.index(min(hdps))
                    elif Q == 2:
                        slovo = 'největší'
                        resp = hdps.index(max(hdps))
                    
                    question = {
                        'answers': ['A: '+name_a,'B: '+name_b,'C: '+name_c,'D: '+name_d],
                        'correct': resp,
                        'question': 'Který z následujících států má '+slovo+' HDP na hlavu podle dat z roku '+str(year)+'?',
                        'source': 'open data OECD',
                        'value': (name_a+': '+str(HDP_a)+' $\r'+name_b+': '+str(HDP_b)+' $\r'+
                                  name_c+': '+str(HDP_c)+' $\r'+name_d+': '+str(HDP_d)+' $\r'+
                                  'pozn.: počítáme celou populaci státu.'),
                        'more_html': ''  }
        
        except:
            return(None)
    else:
        question = None;
    return question
