# pylint: skip-file

from blackjack import generate_deck, points_for, play
from support.testing_util import player_chooses, reset_test_suite, capture_print_lines

"""
Testing Generate Deck
"""


def test_generate_deck():
    completeDeck = [
        'AS',
        '2S',
        '3S',
        '4S',
        '5S',
        '6S',
        '7S',
        '8S',
        '9S',
        '10S',
        'JS',
        'QS',
        'KS',
        'AD',
        '2D',
        '3D',
        '4D',
        '5D',
        '6D',
        '7D',
        '8D',
        '9D',
        '10D',
        'JD',
        'QD',
        'KD',
        'AC',
        '2C',
        '3C',
        '4C',
        '5C',
        '6C',
        '7C',
        '8C',
        '9C',
        '10C',
        'JC',
        'QC',
        'KC',
        'AH',
        '2H',
        '3H',
        '4H',
        '5H',
        '6H',
        '7H',
        '8H',
        '9H',
        '10H',
        'JH',
        'QH',
        'KH'
    ]

    assert generate_deck() == completeDeck


"""
Testing points_for
"""


def test_points_for_empty():
    """points_for() calculates the correct amount of points when no cards are present"""

    assert points_for([]) == 0


def test_points_for_two_cards():
    """points_for() calculates the correct amount of points when only number cards are used"""

    assert points_for(['7H', '2D']) == 9


def test_points_five_cards():
    """points_for() calculates the correct amount of points when only number and face cards are used"""

    assert points_for(['3D', 'JC', 'QH', '2H', 'AC']) == 36


def test_points_two_aces():
    """points_for() calculates the correct amount of points when there are only two aces"""

    assert points_for(['AD', 'AC']) == 21


def test_points_two_aces_plus_one():
    """points_for() calculates the correct amount of points when there are two aces and another card"""

    assert points_for(['2D', 'AD', 'AC']) == 24


"""
Testing gameplay
"""


def test_player_turn_output_hitting(monkeypatch):
    """player_turn(): choosing to hit outputs a "Hitting" message"""

    # The choices that a player will make during the game
    player_chooses(["hit", "stick"], monkeypatch)

    # A tool to capture all of the lines printed in the game
    captured_output = capture_print_lines()

    # Start our game with the given seed
    # All printed lines will be stored inside captured_output in a single string
    play(389813913)

    # Split the messages received into a list of individual lines
    printed_lines = captured_output.getvalue().split("\n")

    # Reset the test suite ready for the next test
    reset_test_suite()

    # Check that the word Hitting is in the list
    assert "Hitting" in printed_lines


def test_player_choosing_hit_updates_hand(monkeypatch):
    """player_turn(): choosing to hit shows an updated hand"""

    player_chooses(["hit", "stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(389813913)

    printed_lines = captured_output.getvalue().split("\n")
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    reset_test_suite()

    assert printed_lines[1] != None
    assert "Your hand is 9S, KS, 9H" in printed_lines[1]


def test_player_choosing_hit_updates_points(monkeypatch):
    """player_turn(): choosing to hit shows an updated point total"""

    player_chooses(["hit", "stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(313131)

    printed_lines = captured_output.getvalue().split("\n")
    print(printed_lines)
    printed_lines = list(
        filter(lambda m: (m.startswith('Your hand is')), printed_lines))

    reset_test_suite()

    assert printed_lines[1] != None
    assert "(14 points)" in printed_lines[1]


def test_player_choosing_hit_updates_points_busts(monkeypatch):
    """player_turn(): hitting and busting displays a 'you lose' message"""

    player_chooses(["hit"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed=1595870164262)

    printed_lines = captured_output.getvalue().split("\n")

    reset_test_suite()

    assert "You lose!" in printed_lines
