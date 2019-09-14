# -*- coding: utf-8 -*-
from random import shuffle, randint
from . import foreign_tourists
from . import populace
from . import sklizen_zemedelskych_plodin
from . import life_expectancy

def get_questions(okres):
    moduls = [
        foreign_tourists,
        populace,
        sklizen_zemedelskych_plodin,
        life_expectancy
    ]

    shuffle(moduls)

    questions = []

    for modul in moduls:
        while True:
            question = modul.get_question(okres)
            if question:
                questions.append(question)
                break
            modul = moduls[randint(0, len(moduls) - 1)]

    return questions


