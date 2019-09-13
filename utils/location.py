# -*- coding: utf-8 -*-
import json

kraje = json.load(open('kraje.json'))
okresy = json.load(open('okresy.json'))


def kraje_name():
    return [row['name'] for row in kraje]


def okresy_name():
    return [row['name'] for row in okresy]


if __name__ == '__main__':
    print(okresy_name())
