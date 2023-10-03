# pylint: skip-file

import sys
from io import StringIO


def player_chooses(choices: list, monkeypatch) -> None:
    """
    Take a list of choices and uses them to feed into the game to test with

    For example, if this is run with ["hit", "stick"] then in the game the player will
    first choose hit and then choose stick.

    Monkeypatch is used to fake (or 'mock') the input from the user
    """
    answers = iter(choices)
    monkeypatch.setattr('builtins.input', lambda name: next(answers))


def reset_test_suite() -> None:
    """
    Reset the test suite, ready to run another test. 
    Should be run at the end of every test
    """
    sys.stdout = sys.__stdout__


def capture_print_lines() -> None:
    """
    Capture all of the lines print'ed by the user during the game so we
    can test if they are correct
    """
    captured_output = StringIO()
    sys.stdout = captured_output
    return captured_output
