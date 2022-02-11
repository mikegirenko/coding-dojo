import random


def one_try_score() -> int:  # number of pins downed in one try (roll)
    number_of_pins_downed = random.randint(0, 10)
    return number_of_pins_downed


def one_frame_score(frame_counter) -> int:  # number of pins downed in one frame (two tries)
    frame_score = 0
    try_one_score = one_try_score()
    try_two_score = one_try_score()
    if frame_counter == 1:
        frame_score = try_one_score + try_two_score
    if frame_counter > 1:
        if (try_one_score + try_two_score) == 10:
            frame_score = 10 + try_one_score
        else:
            frame_score = try_one_score + try_two_score
    return frame_score


def game_score() -> int:
    frame_counter = 1
    game_score_final = 0
    while frame_counter < 11:
        game_score_final += one_frame_score(frame_counter)
        frame_counter += 1
    return game_score_final
