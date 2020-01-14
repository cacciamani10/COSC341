import random
import math
from datetime import datetime


def change(cents):
    result = []
    if cents < 0:
        raise ValueError('amount cannot be negative')
    result.append(cents // 25)
    cents %= 25
    result.append(cents // 10)
    cents %= 10
    result.append(cents // 5)
    result.append(cents % 5)
    return tuple(result)

def strip_quotes(s):
    s = s.replace('"', '')
    return s.replace("'", "")

def scramble(s):
    if scramble.seed:
        random.seed(datetime.now())
        scramble.seed = False
    s = list(s)
    res = ''
    while len(s) > 0:
        x = random.randint(0, len(s) - 1)
        nextLetter = s[x]
        res += nextLetter
        s.remove(nextLetter)
    return res
scramble.seed = True

def powers(base, limit):
    res = []
    if base < 1 or limit < 1:
        return iter(tuple(res))
    exp = 1
    nextPow = 1 
    while nextPow <= limit:
        res.append(nextPow)
        nextPow = base ** exp
        exp += 1
    return iter(tuple(res))

def say(*word):
    if len(word) > 1:
        raise TypeError('input expected at most 1 arguments, got', len(word))
    elif len(word) == 1:
        return say()
    else:
        return say(' ')

def triples(limit):
    res = []
    if limit < 1:
        return res
    for a in range(limit):
        for b in range(1, a):
            c = math.sqrt(a ** 2 + b ** 2)
            #print(a, '+', b, '=', c)
            if int(c) > limit:
                #print('limit surpassed', c, limit)
                return res
            if c == int(c):
                tup = (b, a, int(c))
                #print(tup, 'added')
                res.append(tup)
    return res

print(say('hi')('there')())