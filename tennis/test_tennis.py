from unittest.mock import patch, MagicMock
from tennis.tennis import Tennis

obj = Tennis()


def test_points():
    print(obj.get_point())


def test_game():
    print(obj.game())
