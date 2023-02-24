import random


class Tennis:
    def get_point(self) -> str:
        points = ["love", "15", "30", "40"]
        random_number = random.randint(0, 3)
        point = points[random_number]

        return point

    def game(self):
        score = [0, 0]
        point = ""
        game_over = False
        while not game_over:
            random_number = random.randint(0, 1)
            print("random_number", random_number)
            # generate score
            if random_number == 0:
                score = [1, 0]
            if random_number == 1:
                score = [0, 1]
            if score == [0, 1]: # this exists the game, needs update
                point = 40
                if point == 40:
                    game_over = True

        return score


if __name__ == "__main__":
    obj = Tennis()
    print(obj.get_point())
