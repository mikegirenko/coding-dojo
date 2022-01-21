from bowling_game.code.game import Game


def test_game():
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    assert game_object.return_roll() == roll


