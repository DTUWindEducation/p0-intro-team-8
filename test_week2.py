"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn
import pytest 

def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    fxn.goldilocks(135)
    captured = capsys.readouterr() # Basically capsys is built-in pytest tool that sapture the printed output with capsys
    # then
    assert captured.out == "Too small!\n"
    
    # given
    fxn.goldilocks(155)
    captured = capsys.readouterr()
    # then
    assert captured.out == "Too large!\n"
    

def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 10
    exp_out = [1, 1, 2, 3, 5, 8]
    # when
    out = fxn.fibonacci_stop(inp)
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp = [95, 45, -5]
    status = [True, False, True]
    exp_out = [-999, 45, -999]
    # when
    out = fxn.clean_pitch(inp, status)
    # then
    assert exp_out == out