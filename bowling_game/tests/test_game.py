from bowling_game.code.game import *


def test_number_of_pins_downed_in_one_try():
    assert 0 <= one_try_score() <= 10


def test_score_for_one_frame():
    score_one, _ = one_frame_score()
    _, score_two = one_frame_score()
    score = score_two + score_two
    assert 0 <= score <= 20


def test_game_score():
    score, _ = game_score()
    _, frame_count = game_score()
    assert 0 <= score <= 300
    assert frame_count == 10


# 9- 9- 9- 9- 9- 9- 9- 9- 9- 9- (20 rolls: 10 pairs of 9 and miss) = 10 frames * 9 points = 90
# in two tries player fails to knock all pins down
def test_open_game():
    # TODO use assertion not print
    score, _ = game_score()
    _, frame_count = game_score()
    print("game score is", score)
    print("frame count is", frame_count)
    assert 0 <= score <= 300
    assert frame_count == 10


# 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5 (21 rolls: 10 pairs of 5 and spare, with a final 5) =
# 10 frames * 15 points = 150
# TODO next
def test_spare():
    pass

"""
you if score a spare in the first frame, say an 6 and a 4, then got an 8 and a 1 in the second 
frame, you would score 18 (6+4+8) for the first frame, and 9 for the second frame, making a 
total of 27 after two frames.
"""

"""
This resolved an issue when running a script locally and importing a function from under the 
same project:
PYTHONPATH=`pwd` python test_cases/customer/plan/all_third_parties/test_assessments_widget.py

"""