from blackjack import generate_deck, points_for, play, player_turn, dealer_turn
from support.testing_util import player_chooses, reset_test_suite, capture_print_lines


def test_deck():

    deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD',
            'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
    assert generate_deck() == deck


def test_player_starting_hand(monkeypatch):
    """players_turn(): check to see if player initial hand contains two cards"""

    deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD',
        'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 1)

    printed_lines = captured_output.getvalue().split("\n")
    player_hand = []
    for i in deck:
        if i in printed_lines[5]:
            player_hand.append(i)

    reset_test_suite()

    assert len(player_hand) == 2


def test_dealer_starting_hand(monkeypatch):
    """players_turn(): check to see if player initial hand contains two cards"""

    deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD',
        'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 1)

    printed_lines = captured_output.getvalue().split("\n")
    dealers_hand = []
    for i in deck:
        if i in printed_lines[7]:
            dealers_hand.append(i)

    reset_test_suite()

    print(printed_lines)

    assert len(dealers_hand) == 2

    
def test_dealer_bust(monkeypatch):
    """dealer_turn(): dealer hitting and busting displays 'Dealer busts...' message"""

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 3)

    printed_lines = captured_output.getvalue().split("\n")

    reset_test_suite()

    assert "Dealer busts..." in printed_lines


def test_player_bust(monkeypatch):
    """dealer_turn(): dealer hitting and busting displays 'Dealer busts...' message"""

    player_chooses(['hit', 'hit', 'hit', "stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 5)

    printed_lines = captured_output.getvalue().split("\n")

    print(printed_lines)

    reset_test_suite()

    print(printed_lines)

    assert 'Player busts...' in printed_lines and 'Dealer busts...' not in printed_lines 


def test_player_higher_score_wins(monkeypatch):
    """player_turn(): player wins if they have a higher score than dealer displays 'You scored higher than the dealer!' message"""

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 10)

    printed_lines = captured_output.getvalue().split("\n")

    reset_test_suite()

    assert "You scored higher than the dealer!" in printed_lines


def test_player_lower_score_loses(monkeypatch):
    """player_turn(): player wins if they have a higher score than dealer displays 'You scored lower than the dealer!' message"""

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 2)

    printed_lines = captured_output.getvalue().split("\n")

    reset_test_suite()
    
    assert "You scored lower than the dealer!" in printed_lines

    
def test_player_equal_score_draw(monkeypatch):
    """player_turn(): player wins if they have a higher score than dealer displays 'You scored lower than the dealer!' message"""

    player_chooses(["stick"], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 1)

    printed_lines = captured_output.getvalue().split("\n")

    reset_test_suite()
    
    assert "Draw!" in printed_lines
        

def test_check_turn_order(monkeypatch):
    """player_turn(): check turn order - first the players turn then the dealers turn"""

    player_chooses(['stick'], monkeypatch)

    captured_output = capture_print_lines()

    play(seed = 3)

    printed_lines = captured_output.getvalue().split('\n')
    printed_lines = list(
        filter(lambda m: (m.endswith('begins...')), printed_lines))

    reset_test_suite()

    print(printed_lines)

    assert printed_lines[0] == 'Player turn begins...' and printed_lines[1] == 'Dealers turn begins...'



    

