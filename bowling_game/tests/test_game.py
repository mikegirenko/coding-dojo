from bowling_game.code.game import Game


def test_ten_frame_stopping_game():
    roll = "x"
    game_object = Game(roll)
    for i in range(0, 11):
        game_stopped = game_object.ten_frames_stopping_game(i)
        if i == 10:
            assert game_stopped


def test_two_tries_stopping_frame():
    roll = "x"
    game_object = Game(roll)
    for i in range(0, 3):
        frame_stopped = game_object.two_tries_stopping_frame(i)
        if i == 2:
            assert frame_stopped

def test_generate_pins_creates_three_pins():
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    expected_score = ["x", "/", "-"]
    returned_score = game_object.generate_score()
    assert len(returned_score) == 3


def test_generate_pins_creates_correct_pins():
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    returned_score = game_object.generate_score()
    print("returned_score", returned_score)
    assert any(element in ["x", "/", "-"] for element in returned_score)