from bowling_game.code.game import Game


def test_ten_frames_stopping_game():
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


def test_calculate_score():
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    print("score is", game_object.calculate_score())


def test_frame_result_is_strike():
    """
    the bowler knocks down all pins in one try, and gets ten points
    plus the sum of the next two throws
    """
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    assert game_object.frame_result_is_strike() == 300


def test_frame_result_is_spare():
    """
    the bowler knocks down all ten pins in two tries,
    and gets ten points plus the value of the next throw
    """
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    assert game_object.frame_result_is_spare() == 150


def test_frame_result_is_open():
    """
    where in two tries the bowler knocks down less than ten pins.
    """
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    score = game_object.frame_result_is_open()
    assert 0 < score < 91
