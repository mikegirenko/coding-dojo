import random


class Game:
    def __init__(self, roll):
        self.roll = roll

    def return_roll(self):
        return self.roll

    def ten_frames_stopping_game(self, frame):
        game_over = False
        if frame == 10:
            game_over = True
        return game_over

    def two_tries_stopping_frame(self, tries):
        frame_over = False
        if tries == 2:
            frame_over = True
        return frame_over


    def generate_score(self):
        legit_chars = ["x", "/", "-"]
        score = []
        for i in range(1, 4):
             score.append(legit_chars[random.randint(0, len(legit_chars) - 1)])
        return score


if __name__ == "__main__":
    roll = "x"
    game_object = Game(roll)
    print(game_object.return_roll())
