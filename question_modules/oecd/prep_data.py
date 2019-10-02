#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv,json


if __name__ == '__main__':
    with open('translation.json',encoding='utf-8') as jin:
        translation = json.load(jin) 
    
    src = 'C:\\Users\\Marek.Bohac\\Desktop\\chat-bot-2do\\DP_LIVE_26092019164034862.csv'
    population = {};
    with open(src, newline='', encoding='utf-8') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            if row[2] == 'TOT' and row[3] == 'MLN_PER':
                CCode,year,pop = row[0],int(row[5]),int(1000000*float(row[6]))
                if not year in population:
                    population[year] = {};
                population[year][CCode] = pop;
    
    
    src = 'C:\\Users\\Marek.Bohac\\Desktop\\chat-bot-2do\\SNA_TABLE1_17092019104726297.csv'
    data = {};
    
    with open(src, newline='', encoding='utf-8') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            if row[3] == 'Gross domestic product (output approach)' and row[8] == 'USD':
                HDP,year,val,CCode,country = row[14],int(row[7]),row[10],row[0],row[1]
                HDP = float(HDP)*10**int(val);                
                
                if country in translation:
                    if not year in data:
                        data[year] = {}
                    try:
                        if CCode in population[year]:
                            data[year][country] = [HDP,CCode,country,translation[country],population[year][CCode]]
                    except:
                        if CCode in population[2010]:
                            data[year][country] = [HDP,CCode,country,translation[country],population[2010][CCode]]
        
    
    with open('GDP.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 2, ensure_ascii=False)
    
    ccc = []
    for y in data:
        ccc += list(data[y].keys())
    ccc = list(set(ccc))
    for x in ccc:
        print(x)
    #===========================================================================
    # for d in data
    #     
    #     export do jsonu
    #     
    #===========================================================================
        
        