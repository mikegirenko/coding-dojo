from bowling_game.code.game import *


def test_game():
    score = game_score()
    assert 0 <= score <= 300
