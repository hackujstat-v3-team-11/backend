# -*- coding: utf-8 -*-
import json
import os

__path__ = os.path.dirname(__file__)


kraje = json.load(open(os.path.join(__path__, 'kraje.json')))
okresy = json.load(open(os.path.join(__path__, 'okresy.json')))


def kraje_name():
    return [row['name'] for row in kraje]


def okresy_name():
    return [row['name'] for row in okresy]


def find_okres(name):
    for row in okresy:
        if row['name'] == name:
            return row


def find_kraj(name):
    for row in kraje:
        if row['name'] == name:
            return row


def get_kraj(okres):
    tmp = find_okres(okres)
    if tmp:
        cznuts = tmp['cznuts'][:-1]
        for row in kraje:
            if row['cznuts'] == cznuts:
                return row


if __name__ == '__main__':
    print(okresy_name())
