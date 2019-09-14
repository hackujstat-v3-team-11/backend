from random import randint

def get_key(data):
    keys = list(data.keys())
    i = randint(0, len(keys)-1)
    return keys[i]
