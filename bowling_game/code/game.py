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

    def generate_score(self): # how many pins where knocked down
        legit_chars = ["x", "/", "-"]
        score = []
        for i in range(1, 4):
            score.append(legit_chars[random.randint(0, len(legit_chars) - 1)])
        return score

    def calculate_score(self):
        generated_score = self.generate_score()
        print("generated_score", generated_score)
        score = 0
        for element in generated_score:
            if element == "x":
                score += 1
        return score

    def frame_result_is_strike(self):
        result = "strike"
        score = self.score(result)
        return score

    def frame_result_is_spare(self):
        result = "spare"
        score = self.score(result)
        return score

    def frame_result_is_open(self): # continue
        result = "open"
        score = self.score(result)
        return score

    def generate_open_score(self):
        open_score = random.randint(0, 91)
        return open_score

    def score(self, result):
        if result == "strike":
            score = 300
        if result == "spare":
            score = 150
        if result == "open":
            score = self.generate_open_score()
        return score


if __name__ == "__main__":
    roll = ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
    game_object = Game(roll)
    print(game_object.return_roll())
