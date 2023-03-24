from unittest.mock import patch, MagicMock
from tennis.tennis import Tennis

obj = Tennis()


def test_points():
    point = obj.get_point()
    assert point is not None


def test_game():
    game_score = obj.game()
    assert type(game_score[0]) == int
    assert type(game_score[1]) == int

