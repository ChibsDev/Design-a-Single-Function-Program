from lib.grammar_checker import *
import pytest

def test_returns_true_for_correct_sentence():
    assert grammar_checker("Hello world.") == True

def test_returns_false_if_no_capital_letter_at_start():
    assert grammar_checker("hello world.") == False

def test_returns_false_if_no_punctuation_at_end():
    assert grammar_checker("Hello world") == False

def test_returns_true_with_exclamation_mark():
    assert grammar_checker("Hello world!") == True

def test_returns_true_with_question_mark():
    assert grammar_checker("Hello world?") == True

def test_returns_false_with_wrong_punctuation():
    assert grammar_checker("Hello world,") == False

# EDGE CASES 

def test_grammar_checker_raises_on_none():
    with pytest.raises(Exception) as e:
        grammar_checker(None)
    error_message = str(e.value)
    assert error_message == "Please provide text and I will check your grammar"

def test_returns_false_for_empty_string():
    assert grammar_checker("") == False

def test_returns_false_for_string_with_only_whitespace():
    assert grammar_checker(" ") == False


