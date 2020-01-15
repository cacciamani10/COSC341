# h1.py
# Jacob Cacciamani
# 01/19/20
# COSC 341
import random
from datetime import datetime

# Takes a parameter cents and returns a tuple
# containing quarters, dimes, nickels, and pennies respectively
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

# Removes quotes from the passed string parameter
def strip_quotes(s):
    s = s.replace('"', '')
    return s.replace("'", "")

# Psuedo-randomly swaps characters until the string is scrambled up
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

# Returns an iterator for a tuple
# of a series of powers based on parameters
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

# A recursive function with an inner lambda
def say(word=''):
    if word == '': 
        return word
    return lambda y=None: word if y is None else say(word + ' ' + y)
    
# Returns a sorted list of all pythagorean triples
# under a limit
def triples(limit):
    res = []
    if limit < 1:
        return res
    for c in range(1, limit + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a * a + b * b == c * c:
                    tup = (a, b, c)
                    res.append(tup)
    res.sort(key = lambda tup: tup[0])
    return res