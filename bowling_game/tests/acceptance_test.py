from bowling_game.code.game import *


def test_game():
    score, _ = game_score()
    _, frame_count = game_score()
    assert 0 <= score <= 300
    assert frame_count == 10
