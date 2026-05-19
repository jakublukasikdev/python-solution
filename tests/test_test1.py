import pytest
from test1 import shared_words

def test_basic():
    a = ['century', 'customer', 'democratic', 'Congress', 'customer', 'evening',
         'often', 'outside', 'reveal', 'weight', 'western', 'century']
    b = ['weapon', 'western', 'traditional', 'guess', 'customer', 'exist',
         'democratic', 'Congress', 'evening', 'finish', 'western', 'executive']
    result = shared_words(a, b)
    assert result == sorted(set(a) & set(b), key=len)

def test_no_common():
    assert shared_words(['a', 'b'], ['c', 'd']) == []

def test_duplicates_removed():
    result = shared_words(['hi', 'hi'], ['hi'])
    assert result.count('hi') == 1

def test_sorted_by_length():
    result = shared_words(['ab', 'abcd', 'abc'], ['ab', 'abcd', 'abc'])
    lengths = [len(w) for w in result]
    assert lengths == sorted(lengths)
