import random


class Tennis:
    def get_point(self) -> str:
        points = ["love", "15", "30", "40"]
        random_number = random.randint(0, 3)
        point = points[random_number]

        return point

    def game(self) -> list:
        player_one_points = 0
        player_two_points = 0
        game_continues = True
        game_counter = 0
        while game_continues and game_counter < 7:
            random_number = random.randint(1, 2)  # 1 for player 1; 2 for player 2
            if random_number == 1:
                player_one_points += 1
            if random_number == 2:
                player_two_points += 1
            if (player_one_points - player_two_points == 2) or (
                player_two_points - player_one_points == 2
            ):
                if player_one_points == 4 or player_two_points == 4:
                    game_continues = False
                else:
                    game_continues = True
            else:
                if (player_one_points - player_two_points == 2) or (
                    player_two_points - player_one_points == 2
                ):
                    game_continues = False
                else:
                    game_continues = True
            game_counter += 1
        score = [player_one_points, player_two_points]

        return score


if __name__ == "__main__":
    obj = Tennis()
    who_won = ""
    score = obj.game()
    if score[0] > score[1]:
        who_won = "Player 1"
    if score[1] > score[0]:
        who_won = "Player 2"
    print("Score is", score[0], ":", score[1], ".", who_won, "won.")
