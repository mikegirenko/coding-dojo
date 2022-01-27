from bowling_game.code.game import *


def test_number_of_pins_downed_in_one_try():
    assert 0 <= number_of_pins_downed_in_one_try() <= 10


def test_score_for_one_frame():
    score = score_for_one_frame()
    assert 0 <= score <= 20


def test_game_score():
    assert 0 <= game_score() <= 300


# 9- 9- 9- 9- 9- 9- 9- 9- 9- 9- (20 rolls: 10 pairs of 9 and miss) = 10 frames * 9 points = 90
# in two tries player fails to knock all pins down
def test_open_game():
    print(game_score())

