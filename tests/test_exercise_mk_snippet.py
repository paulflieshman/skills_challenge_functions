import pytest
from lib.exercise_mk_snippet import *

def test_return_string():


# given a string
# it returns the string

    result = make_snippet("One Two Three Four")
    assert result == ("One Two Three Four")


# given a string of more than 5 words is caught by the function
# return the string only if 5 words or under

# def test_return_string_five_or_more():
#     result = make_snippet("One Two Three Four Five Six")
#     assert result == None


def test_return_string_five_or_more_truncated():
    result = make_snippet("One Two Three Four Five Six")
    assert result == make_snippet("One Two Three Four Five...")

