from lib.grammar_checker import *

def test_returns_true_for_correct_sentence():
    assert grammar_checker("Hello world.") == True

def test_returns_false_if_no_capital_letter_at_start():
    assert grammar_checker("hello world.") == False

def test_returns_false_if_no_punctuation_at_end():
    assert grammar_checker("Hello world") == False