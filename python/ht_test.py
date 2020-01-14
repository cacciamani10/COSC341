import re
import math
import pytest
from h1 import (change, strip_quotes, scramble, say, triples, powers)

def test_change():
    assert change(0) == (0, 0, 0, 0)
    assert change(97) == (3, 2, 0, 2)
    assert change(8) == (0, 0, 1, 3)
    assert change(250) == (10, 0, 0, 0)
    assert change(144) == (5, 1, 1, 4)
    assert change(97) == (3, 2, 0, 2)
    assert change(100000000000) == (4000000000, 0, 0, 0)
    with pytest.raises(ValueError) as excinfo:
        change(-50)
    assert str(excinfo.value) == 'amount cannot be negative'

def test_strip_quotes():
    assert strip_quotes('') == ''
    assert strip_quotes('Hello, world') == 'Hello, world'
    assert strip_quotes('"\'') == ''
    assert strip_quotes('a"""\'\'"z') == 'az'

def test_scramble():
    for s in ['a', 'rat', 'JavaScript testing', '', 'zzz', '^*))^*>^▱ÄÈËɡɳɷ']:
        assert sorted(s) == sorted(scramble(s))
    possibilities = set(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])
    for _ in range(200):
        possibilities.discard(scramble('ABC'))
    assert not possibilities

def test_say():
    assert say() == ''
    assert say('hi')() == 'hi'
    assert say('hi')('there')() == 'hi there'
    assert say('hello')('my')('name')('is')('Colette')() == 'hello my name is Colette'

def test_triples():
    assert triples(0) == []
    assert triples(5) == [(3, 4, 5)]
    assert set(triples(40)) == set([(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
                                    (9, 12, 15), (10, 24, 26), (12, 16, 20), (12, 35, 37),
                                    (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30),
                                    (20, 21, 29), (21, 28, 35), (24, 32, 40)])

def test_powers():
    p = powers(2, 10)
    assert next(p) == 1
    assert next(p) == 2
    assert next(p) == 4
    assert next(p) == 8
    with pytest.raises(StopIteration):
        next(p)
    assert list(powers(2, -5)) == []
    assert list(powers(7, 0)) == []
    assert list(powers(3, 1)) == [1]
    assert list(powers(2, 63)) == [1, 2, 4, 8, 16, 32]
    assert list(powers(2, 64)) == [1, 2, 4, 8, 16, 32, 64]