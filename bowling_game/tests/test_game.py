from bowling_game.code.game import *
"""
Acceptance Criteria - a Strike
"""

# X X X X X X X X X X X X (12 rolls: 12 strikes) = 10 frames * 30 points = 300


def test_number_of_pins_downed_in_one_try():
    assert 0 <= number_of_pins_downed_in_one_try() <= 10


def test_number_of_pins_downed_in_one_frame():
    number_of_pins = number_of_pins_downed_in_one_frame()
    try_one = number_of_pins[0]
    try_two = number_of_pins[1]
    assert 0 <= try_one <= 10
    assert 0 <= try_two <= 10


def test_score_for_one_frame():
    score = score_for_one_frame()
    assert 0 <= score <= 20


def test_game_score():
    assert 0 <= game_score() <= 300
