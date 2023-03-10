import random


class Tennis:
    def get_point(self) -> str:
        points = ["love", "15", "30", "40"]
        random_number = random.randint(0, 3)
        point = points[random_number]

        return point

    def game(self):
        score = [0, 0]
        game_score = [0, 0]
        point = 0
        player_one_points = 0
        player_two_points = 0
        while point < 4:
            random_number = random.randint(1, 2)  # player 1 and player 2
            print("random_number", random_number)
            # generate score
            if random_number == 1:
                player_one_points += 1
            if random_number == 2:
                player_two_points += 1
            point += 1
            print(score)
        print("player_one_points", player_one_points)
        print("player_two_points", player_two_points)
        return score


if __name__ == "__main__":
    obj = Tennis()
    print(obj.get_point())


    # def game(self):
    #     score = [0, 0]
    #     point = ""
    #     player_one_points = 0
    #     player_two_points = 0
    #     game_over = False
    #     while not game_over:
    #         random_number = random.randint(0, 1)
    #         print("random_number", random_number)
    #         # generate score
    #         if random_number == 0:
    #             score = [1, 0]
    #             player_one_points += 1
    #         if random_number == 1:
    #             score = [0, 1]
    #             player_two_points += 1
    #
    #         print("player_one_points", player_one_points)
    #         print("player_two_points", player_two_points)
    #         game_over = True
    #
    #     return score