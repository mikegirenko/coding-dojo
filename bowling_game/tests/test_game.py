from unittest.mock import patch

from bowling_game.code.game import *


def test_number_of_pins_downed_in_one_try():
    assert 0 <= one_try_score() <= 10


def test_score_for_one_frame():
    score_one = one_try_score()
    score_two = one_try_score()
    score = score_two + score_two
    assert 0 <= score <= 20


def test_game_score_range():
    score = game_score()
    assert 0 <= score <= 300


@patch("bowling_game.code.game.one_try_score")
def test_game_is_all_open_frames(mocked_one_try_score):
    mocked_one_try_score.return_value = 3
    score = game_score()
    assert score == 60


@patch("bowling_game.code.game.one_try_score")
def test_game_is_all_spares(mocked_one_try_score):
    mocked_one_try_score.return_value = 5
    score = game_score()
    assert score == 145


@patch("bowling_game.code.game.one_try_score")
def test_game_is_all_strikes(mocked_one_try_score):
    mocked_one_try_score.return_value = 10
    score = game_score()
    assert score == 200
