# -*- coding: utf-8 -*-
from random import shuffle, randint
from . import foreign_tourists
from . import populace
from . import sklizen_zemedelskych_plodin
from . import life_expectancy
from . import hospodarska_zvirata
from . import people
from . import medical_facilities
from . import ubytek_pudy
from . import jokes_and_riddles
from . import oecd

def get_questions(okres, count=None):
    moduls = [
        foreign_tourists,
        populace,
        sklizen_zemedelskych_plodin,
        life_expectancy,
        hospodarska_zvirata,
        people,
        people,
        medical_facilities,
        ubytek_pudy,
        jokes_and_riddles,
        oecd
    ]

    shuffle(moduls)

    questions = []
    question_text = {}

    if count:
        moduls = moduls[:count]

    for modul in moduls:
        while True:
            question = modul.get_question(okres)
            if question and question['question'] not in question_text:
                questions.append(question)
                question_text[question['question']] = 1
                break
            modul = people

    return questions
